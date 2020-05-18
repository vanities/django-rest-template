# Django Initialization

An admin ui to manage data from a browser ([local](http://127.0.0.1:8000)) and an API to expose data.


## Installation:

1. Get Docker

2. Clone the repository
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
$ docker-compose run --rm test ./manage.py test app.user.tests
```

## Endpoints:

If the server is running execute the following command:
```bash
$ open http://0.0.0.0:8000/docs
```

### Authors

See the list of [contributors](https://github.com/vanities/django-init/graphs/contributors) who participated in this project.

## Adding Python packages

Add the package to the `requirements.txt` (if you know the version) then run.
