import os

is_heroku = False

if 'DYNO' in os.environ:
    is_heroku = True

if is_heroku:
    db_path = os.environ.get('DATABASE_URL')
else:
    db_path = 'sqlite:///passwd.db'