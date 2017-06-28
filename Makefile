.PHONY: tmp

DOCKER=$(shell which docker)
DOCKER_COMPOSE=$(shell which docker-compose)
CONTAINER_NAME=0-deep-learning

tmp:
	mkdir -p tmp

up:
	$(DOCKER_COMPOSE) up -d

build:
	$(DOCKER_COMPOSE) build

clean: stop rm

attach:
	@$(DOCKER) exec -it $(CONTAINER_NAME) bash

stop:
	$(DOCKER_COMPOSE) stop

rm:
	$(DOCKER_COMPOSE) rm -f

python:
	@$(DOCKER) exec -i $(CONTAINER_NAME) python $(SRC)

