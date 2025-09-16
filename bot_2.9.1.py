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

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(
            token=TOKEN,
            prefix="!",
            nick=NICK,
            initial_channels=[CHANNEL],
        )

    async def event_ready(self):
        print(f"Bot {NICK} connected and ready.")

    async def event_join(self, channel, user):
        if user.name.lower() == NICK.lower():
            print(f"Joined channel {channel.name}")
            await channel.send("!join")
            self.loop.create_task(self.catch_task(channel))

    async def catch_task(self, channel):
        while True:
            if POST_INTERVAL == "random":
                wait_time = random.randint(300, 600)  # 5–10 Minuten
            else:
                wait_time = int(POST_INTERVAL)
            await asyncio.sleep(wait_time)
            print("post")
            await channel.send("!catch")

bot = Bot()
bot.run()
