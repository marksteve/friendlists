from setuptools import setup


setup(
    name='friendlists',
    version='0.0.0',
    url='https://github.com/marksteve/friendlists',
    license='MIT',
    author='Mark Steve Samson',
    author_email='hello@marksteve.com',
    description='Manage your Facebook friendlists',
    long_description=__doc__,
    packages=['friendlists'],
    zip_safe=False,
    platforms='any',
    install_requires=[
        'Flask==0.9',
        'requests<1.0',
        'fboauth2',
    ],
    classifiers=[
    ],
)
