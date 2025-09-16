import os
import asyncio
import random
from twitchio.ext import commands
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("TWITCH_TOKEN")
NICK = os.getenv("TWITCH_NICK")
CHANNEL = os.getenv("TWITCH_CHANNEL")
POSTING_INTERVAL_SECONDS = os.getenv("POSTING_INTERVAL_SECONDS")

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=TOKEN, prefix="!", nick=NICK, initial_channels=[CHANNEL])

    async def event_ready(self):
        print(f"Bot {NICK} ready!")
        # Einmal !join senden beim Start
        chan = self.get_channel(CHANNEL)
        if chan:
            await chan.send("!join")
        # Startet den Hintergrundtask für !catch
        self.loop.create_task(self.catch_task(chan))

    async def catch_task(self, channel):
        while True:
            wait_time = POSTING_INTERVAL_SECONDS
            #wait_time = random.randint(300, 600)  # 5-10 Minuten
            await asyncio.sleep(wait_time)
            await channel.send("!catch")

bot = Bot()
bot.run()
