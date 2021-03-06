WTF_CSRF_ENABLED = True
SECRET_KEY = '\x13*\xbb\xe6\xdf\x10!S\xf9\xf6Q\xf5\\\xdb$<j\x8c\xb6\xb3\x08\x12\xe4\x9c'

OPENID_PROVIDERS = [
	{'name': 'Yahoo', 'url': 'https://me.yahoo.com'},
	{'name': 'AOL', 'url': 'http://openid.aol.com/<username>'},
	{'name': 'Flickr', 'url': 'http://www.flickr.com/<username>'},
	{'name': 'MyOpenID', 'url': 'https://www.myopenid.com'}]

import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
