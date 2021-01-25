from discord.ext.commands import Bot as BotBase
from glob import glob
import apscheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Embed, File
from datetime import datetime
from discord.ext.commands import CommandNotFound
from discord.ext.commands import Context
from ..db import db
from apscheduler.triggers.cron import CronTrigger
from asyncio import sleep
import os

PREFIX = "+"
OWNER_IDS = [618038532665114624]
COGS = [path.split(os.sep)[-1][:-3] for path in glob("./lib/cogs/*.py")]

class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)

    def ready_up(self, cog):
        setattr(self, cog, True)
        print(f"{cog} is Ready!")

    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])


class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()


        db.autosave(self.scheduler)
        super().__init__(command_prefix=PREFIX, OWNER_IDS=OWNER_IDS)

        super().__init__(command_prefix = PREFIX, owner_ids = OWNER_IDS)

    def setup(self):
        for cog in COGS:
            print(cog)
            self.load_extension(f"lib.cogs.{cog}")
            print(f"{cog} was loaded!")

        print("Setup Completed!")

    def run(self, version):
        self.VERSION = version

        print("Running Setup...")
        self.setup()


        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("Running bot...")
        super().run(self.TOKEN, reconnect=True)

    async def process_commands(self, message):
        ctx = await self.get_context(message, cls = Context)

        if ctx.command is not None and ctx.guild is not None:
            if self.ready:
                    await self.invoke(ctx)

            else:
                await ctx.send("I'm not listening to your commands you psycho, maybe later...")

    async def print_message(self):
        await self.stdout.send("Good Morning!")

    async def on_connect(self):
        print("BOT has been CONNECTED!")

    async def on_disconnect(self):
        print("BOT has been DISCONNECTED!")

    async def on_error(self, err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("Something went wrong!")

        else:
            channel = self.stdout
            await channel.send("Dude your code freaking sucks, and error occured right here!")

        raise

    async def on_command_error(self, ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass

        elif hasattr(exc, "original"):
            raise exc.original

        else:
            raise exc

    async def on_ready(self):
        if not self.ready:
            self.channel = self.get_channel(801899005411197018)
            self.ready = True
            self.cogs_ready = Ready()
            self.guild = self.get_guild(801895525263343656)
            self.stdout = self.get_channel(801895525263343656)
            self.scheduler.add_job(self.print_message, CronTrigger(day_of_week=0, hour=12, minute=0, second=0))
            self.scheduler.start()

            while self.cogs_ready.all_ready():
                await sleep(0.5)



        else:
            print("BOT reconnected!")

    async def on_message(self, message):
        if not message.author.bot:
            await self.process_commands(message)

bot = Bot()