from fboauth2 import FBClient
from flask import Flask, redirect, url_for, request, session, render_template


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('friendlists.config')
app.config.from_pyfile('application.cfg', silent=True)


def get_fb_client(**kwargs):
    access_token = session.get('access_token')
    if access_token:
        kwargs['access_token'] = access_token
    return FBClient(app.config['FB_APP_ID'], app.config['FB_APP_SECRET'],
                    **kwargs)


@app.route('/login')
def login():
    scope = 'read_friendlists,manage_friendlists'
    redirect_uri = url_for('login', _external=True)
    fb = get_fb_client(scope=scope, redirect_uri=redirect_uri)

    code = request.args.get('code')
    if code:
        session['access_token'] = fb.get_access_token(code)
        session['user'] = fb.graph_request('me')
        return redirect(url_for('index'))

    return redirect(fb.get_auth_url())


@app.route('/logout')
def logout():
    session.pop('access_token')
    session.pop('user')
    return redirect(url_for('index'))


def get_paged_results(fb, path):
    response = fb.graph_request(path)
    while response.get('data'):
        for item in response['data']:
            yield item
        if not response.get('paging'):
            break
        if not response['paging'].get('next'):
            break
        response = fb.request(response['paging']['next'])


@app.route('/')
@app.route('/l/<friendlist_id>', methods=['GET', 'POST'])
def index(friendlist_id=None):
    if 'user' not in session or 'access_token' not in session:
        return render_template('index.html')

    fb = get_fb_client()

    listed = []

    if friendlist_id:
        listed = list(
            get_paged_results(fb, '%s/members' % friendlist_id)
            )
        if request.method == 'POST':
            old_listed = set([f['id'] for f in listed])
            new_listed = set(request.json.get('listed', []))

            removed = old_listed - new_listed
            added = new_listed - old_listed

            if removed:
                fb.graph_request('%s/members' % friendlist_id, method='delete',
                                 params=dict(members=','.join(removed)))

            if added:
                fb.graph_request('%s/members' % friendlist_id, method='post',
                                 params=dict(members=','.join(added)))

            return 'ok'

    friends = list(get_paged_results(fb, 'me/friends'))

    data = dict(friendlist_id=friendlist_id,
                friendlists=list(get_paged_results(fb, 'me/friendlists')),
                friends=friends,
                listed=listed,
                unlisted=[f for f in friends if f not in listed])

    return render_template('app.html', **data)
