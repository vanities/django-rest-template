.PHONY: build up down migrate seed_db test psql shell fresh migrate seed_db reset_db wait_for_postgres upgrade_all_python_dependencies

init:
	pip3 install pre-commit
	pre-commit install
	make build
	make fresh

build:
	docker-compose build

up: build
	docker-compose up django

down:
	docker-compose down --remove-orphans

test: migrate
	docker-compose run --rm test ./manage.py test --parallel
	make down

psql:
	docker-compose run --rm python ./manage.py dbshell

shell:
	docker-compose run --rm python ./manage.py shell

fresh:
	docker-compose down -v
	docker-compose up -d postgres
	make reset_db
	make migrate
	make seed_db

migrate: build wait_for_postgres
	docker-compose run --rm python ./scripts/make_and_migrate

seed_db: wait_for_postgres
	docker-compose run --rm python ./scripts/seed_database

reset_db: wait_for_postgres
	docker-compose run --rm python ./manage.py reset_db --noinput

wait_for_postgres:
	docker-compose run --rm python ./scripts/wait_for_postgres

startapp:
	docker-compose run --rm python ./manage.py startapp

# WARNING, this will upgrade everything to the latest version!
upgrade_all_python_dependencies:
	docker-compose run --rm python bash -c "sed -i 's/==/>=/' requirements.txt && \
	 										pip install --upgrade --force-reinstall -r requirements.txt && \
											pip freeze | sed 's/>=/==/' > requirements.txt"

graph_models:
	docker-compose run --rm python ./manage.py graph_models -a -g -o models.png
