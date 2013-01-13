from setuptools import setup


setup(
    name='friendlists',
    version='0.1.0',
    url='https://github.com/marksteve/friendlists',
    license='MIT',
    author='Mark Steve Samson',
    author_email='hello@marksteve.com',
    description='Manage your Facebook friendlists',
    long_description=__doc__,
    packages=['friendlists'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask==0.9',
        'requests<1.0',
        'fboauth2',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Internet :: WWW/HTTP :: WSGI',
        'Topic :: Internet :: WWW/HTTP :: WSGI :: Application',
    ],
)
