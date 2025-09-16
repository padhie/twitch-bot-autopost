remove:
	docker image rm twitch-bot || true

build:
	docker build -t twitch-bot .

rebuild: remove build

run:
	docker run --rm -it --env-file .env twitch-bot python bot_2.9.1.py