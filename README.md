# twitch autopost bot

## Get oauth token
Hinweis: Du brauchst einen Twitch OAuth Token für deinen Bot. Den kannst du hier generieren: https://twitchapps.com/tmi/


## docker container

### build
docker build -t twitch-bot .

### run
docker run -d --env-file .env twitch-bot


## ChatGPT conversation
https://chatgpt.com/share/68c93429-aac4-800d-aedf-bc0693249b6a