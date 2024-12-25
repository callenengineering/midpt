up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

dev-build:
	docker-compose -f docker-compose.dev.yml build

dev-up:
	docker-compose -f docker-compose.dev.yml up -d

dev-down:
	docker-compose -f docker-compose.dev.yml down

dev-logs:
	docker-compose -f docker-compose.dev.yml logs -f

dev-rebuild: dev-down dev-build dev-up dev-logs
