# news-site
repo for test python task
# QuickStart:
- `python -m venv venv`
- activate venv
- `pip install -r requirements.txt`
- `python manage.py runserver`

# Working with Redis and Celery:
- call redis server: `redis-server` in project folder
- start celery (using gevent): `celery -A news_site worker -l info -P gevent`

# Run tests:
- `python manage.py test`

# About project:
- working with news and posts
- every user post needs to be accepted by the admin or moderator
- there are 3 groups in admin page: `user, moderator, admin`
- you need to verify your account with email

# Super user for test:
- email: `admin@admin.com`
- password: `admin`
