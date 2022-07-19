# Django Initialization

A quick way to up a django server. Has an admin ui to manage data from a browser ([local](http://127.0.0.1:5000)) and an API to expose data. Includes Singleton models for configuration using django-solo, static file uploading with whitenoise, performance monitoring with django-silk, and jwt auth using djangorestframework-simplejwt. Has pre-commit hooks to lint and fix and a setup for github actions to run tests. See the admin on heroku here: [https://django-rest-template.herokuapp.com/](https://django-rest-template.herokuapp.com/).

## Requirements:
1. [pre-commit](https://pre-commit.com/)
2. [docker & docker-compose](https://www.docker.com/products/docker-desktop/)

## Installation:

Clone the repository and initialize
```bash
$ git clone https://github.com/vanities/django-init
$ cd django-init
$ make init
```

## Running the web API:

The [`Makefile`](https://github.com/vanities/django-init/blob/master/Makefile) is a task manager to wrap docker commands, read it to know what the common tasks are.

Quickstart with Docker:
```bash
$ make up
```

Quit the server:
```bash
$ make down
```

Drop and Seed the database:
```bash
$ make fresh
```

## Testing:

To run all of the tests once with Docker:
```bash
$ make test
```

To run a single test file:
```bash
$ docker-compose run --rm test ./manage.py test user.tests
```

## Creating a new app, typically apps are plural ex: *features*:
```bash
$ docker-compose run --rm python ./manage.py startapp features
```

See the list of [contributors](https://github.com/vanities/django-init/graphs/contributors) who participated in this project.

## Adding Python packages

1. find the package on [pypi](https://pypi.org/search/?q=pyyaml&o=)
2. find the version, for the example above, pyyaml is 6.0
3. pyyaml==6.0 to `requirements.txt`
4. run `make build`
