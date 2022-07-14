# Django Initialization

A quick way to up a django server. Has an admin ui to manage data from a browser ([local](http://127.0.0.1:5000)) and an API to expose data. Includes Singleton models for configuration using django-solo, static file uploading with whitenoise, performance monitoring with django-silk, and jwt auth using djangorestframework-simplejwt. Has pre-commit hooks to lint and fix and a setup for github actions to run tests. See the admin on heroku here: [https://django-rest-template.herokuapp.com/](https://django-rest-template.herokuapp.com/).

## Requirements:
1. [pre-commit](https://pre-commit.com/)
2. [docker & docker-compose](https://www.docker.com/products/docker-desktop/)

## Installation:

1. Clone the repository
```bash
$ git clone https://github.com/vanities/django-init
$ cd django-init
```

## Running the web/API:

Generally, we use a [`Makefile`](https://github.com/vanities/django-init/blob/master/Makefile) as a task manager to wrap docker commands, read it to know what the common tasks are.

Quickstart with Docker:
```bash
$ make up
```

Quit the server:
```bash
$ make down
```

Seed the database:
```bash
$ make fresh
```

With python:
```bash
$ python manage.py runserver
```

## Testing:

To run once with Docker:
```bash
$ make test
# or
$ docker-compose run test python manage.py test
```

To run a single test file:
```bash
$ docker-compose run --rm test ./manage.py test user.tests
```

## Endpoints:

If the server is running execute the following command:
```bash
$ open http://127.0.0.1:8000/docs
```

### Authors

See the list of [contributors](https://github.com/vanities/django-init/graphs/contributors) who participated in this project.

## Adding Python packages

Add the package to the `requirements.txt`
