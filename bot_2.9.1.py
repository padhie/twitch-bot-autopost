import os
import asyncio
import random
from twitchio.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TWITCH_TOKEN")
NICK = os.getenv("TWITCH_NICK")
CHANNEL = os.getenv("TWITCH_CHANNEL")
POST_INTERVAL = os.getenv("POSTING_INTERVAL_SECONDS")
JOIN_COMMAND = os.getenv("JOIN_COMMAND")
INTERVAL_COMMAND = os.getenv("INTERVAL_COMMAND")
INTERVAL_COMMAND_MIN = int(os.getenv("POSTING_INTERVAL_SECONDS_MIN"))
INTERVAL_COMMAND_MAX = int(os.getenv("POSTING_INTERVAL_SECONDS_MAX"))

wait_time = random.randint(INTERVAL_COMMAND_MIN, INTERVAL_COMMAND_MAX)

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            token=TOKEN,
            nick=NICK,
            prefix="",
            initial_channels=[CHANNEL],
        )

    async def event_ready(self):
        print(f"Bot {NICK} connected and ready.")

    async def event_join(self, channel, user):
        if user.name.lower() == NICK.lower():
            print(f"Joined channel {channel.name}")
            if JOIN_COMMAND != "":
                await channel.send(JOIN_COMMAND)
            if wait_time != 0:
                self.loop.create_task(self.catch_task(channel))

    async def catch_task(self, channel):
        while True:
            await asyncio.sleep(wait_time)
            print(f"post {INTERVAL_COMMAND} command")
            await channel.send(INTERVAL_COMMAND)

bot = Bot()
bot.run()
