SERVER_NAME ?= localhost

help: ## show this help
	@echo 'usage: make [target] ...'
	@echo ''
	@echo 'targets:'
	@egrep '^(.+)\:\ .*##\ (.+)' ${MAKEFILE_LIST} | sed 's/:.*##/#/' | column -t -c 2 -s '#'

build:  ## build dev image
	docker-compose build

dev:  ## start in dev mode
	SERVER_NAME=$(SERVER_NAME) docker-compose up --force-recreate --remove-orphans -d
	docker-compose logs -f

test: ## run python tests in dev container
	docker-compose run --rm backend nosetests --with-coverage --cover-package app tests/
