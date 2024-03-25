build:
	docker-compose build

run:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

clean:
	docker-compose down --remove-volumes

bash:
	docker-compose run --rm bot bash

ps:
	docker ps
restart:
	make down
	make build
	make run
	make logs


.PHONY: build up down logs bash clean
