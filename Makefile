SHELL := /bin/bash

# ifeq (,$(wildcard .envs/.production/.django))
#     $(error no .envs/.production/.django file located.)
# endif


help:
	@$(MAKE) -pRrq -f $(lastword $(MAKEFILE_LIST)) : 2>/dev/null | awk -v RS= -F: '/^# File/,/^# Finished Make data base/ {if ($$1 !~ "^[#.]") {print $$1}}' | sort | egrep -v -e '^[^[:alnum:]]' -e '^$@$$'

migrations:
	docker-compose -f local.yml run --rm django python manage.py makemigrations

migrate:
	docker-compose -f local.yml run --rm django python manage.py migrate

superuser:
	docker-compose -f local.yml run --rm django python manage.py createsuperuser

build:
	docker-compose -f local.yml build

up:
	docker-compose -f local.yml up

down:
	docker-compose -f local.yml down

shell:
	docker-compose -f local.yml run --rm django python manage.py shell

collectstatic:
	docker-compose -f local.yml run --rm django python manage.py collectstatic

rebuild:
	make down && git pull && make build && make up

gulp:
	docker-compose -f local.yml run --rm node gulp

setup:
	git pull && make build && make migrations && make migrate && make up

#
# this is for the production environment
#

pro-migrations:
	docker-compose -f production.yml run --rm django python manage.py makemigrations

pro-migrate:
	docker-compose -f production.yml run --rm django python manage.py migrate

pro-superuser:
	docker-compose -f production.yml run --rm django python manage.py createsuperuser

pro-build:
	docker-compose -f production.yml build

pro-up:
	docker-compose -f production.yml up -d

pro-down:
	docker-compose -f production.yml down

pro-shell:
	docker-compose -f production.yml run --rm django python manage.py shell

pro-collectstatic:
	docker-compose -f production.yml run --rm django python manage.py collectstatic

pro-rebuild:
	make pro-down && git pull && make pro-build && make pro-up