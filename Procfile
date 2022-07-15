release: ./manage.py migrate && ./manage.py collectstatic --no-input
web: gunicorn config.wsgi
