# Django Initialization

A quick way to up a django rest server. Has an admin ui to manage data from a browser ([local](http://127.0.0.1:5000)) and an API to expose data.
Superuser/staff user and seed creation is in [scripts/seed_database](https://github.com/vanities/django-rest-template/blob/master/scripts/seed_database).

Username: **admin**<br>
Password: **password123**

See the admin on heroku here: [https://django-rest-template.herokuapp.com/](https://django-rest-template.herokuapp.com/).

## Packages:
1. Singleton models for configuration using [django-solo](https://github.com/lazybird/django-solo).
2. Static file uploading with [whitenoise](https://github.com/evansd/whitenoise).
3. Performance monitoring with [django-silk](https://github.com/jazzband/django-silk).
4. JWT authentication using [djangorestframework-simplejwt](https://github.com/jazzband/djangorestframework-simplejwt).
5. Has [pre-commit](https://github.com/pre-commit/pre-commit) hooks to lint and fix files using Black and flake8.
6. Setup for [github actions](https://github.com/features/actions) to run tests.
7. Model graph visualization with [pygraphviz](https://gist.github.com/rg3915/35e999a442a8955e455b).
8. CORS handling based on environment variables by [django-cors-headers](https://github.com/adamchainz/django-cors-headers).
9. Abstact user models set up in `users/`

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
