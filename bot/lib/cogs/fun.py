import sys
from random import choice, randint
from typing import Optional

from discord import Member, File
from discord.ext.commands import Cog
from discord.ext.commands import command

OWNERS = ["618038532665114624", "623772185315639302"]


class Fun(Cog):
    def __init__(self, bot):
        self.bot = bot
        self.isOn = False

    #######################################################
    ################# ADMIN PERMISSIONS ###################
    #######################################################
    @command(name="enable", aliases=["on", "activate"])
    async def turn_on(self, ctx):
        if (str(ctx.message.author.id) in OWNERS):
            self.isOn = True
            await ctx.send("BOT COMMANDS ARE ON, PLEASE DO NOT KILL MY FUCKING DRONE <3")
            print(self.isOn)
            return self.isOn

    @command(name="disable", aliases=["off", "deactivate"])
    async def turn_off(self, ctx):
        if (str(ctx.message.author.id) in OWNERS):
            await ctx.send("BOT COMMANDS ARE OFF. BITCH, STOP SPAMMING, TY <3")
            self.isOn = False
            return self.isOn

    #######################################################
    #######################################################

    #######################################################
    #################### USER COMMANDS ####################

    @command(name="forward", aliases=["ireli"])
    async def forward(self, ctx):
        print(self.isOn)
        if self.isOn:
            await ctx.send("Forward")
            return True
        else:
            await ctx.send("Owners have not enabled the commands yet!")
            return False

    @command(name="backward", aliases=["geri"])
    async def backward(self, ctx):
        if self.isOn:
            await ctx.send("Backward")
            return True
        else:
            await ctx.send("Owners have not enabled the commands yet!")
            return False

    @command(name="up", aliases=["yukari"])
    async def up(self, ctx):
        if self.isOn:
            await ctx.send("Up")
            return True
        else:
            await ctx.send("Owners have not enabled the commands yet!")
            return False

    @command(name="down", aliases=["asagi"])
    async def down(self, ctx):
        if self.isOn:
            await ctx.send("Down")
            return True
        else:
            await ctx.send("Owners have not enabled the commands yet!")
            return False

    @command(name="right", aliases=["saga"])
    async def right(self, ctx):
        if self.isOn:
            await ctx.send("Right")
            return True
        else:
            await ctx.send("Owners have not enabled the commands yet!")
            return False

    @command(name="left", aliases=["sola"])
    async def left(self, ctx):
        if self.isOn:
            await ctx.send("Left")
            return True
        else:
            await ctx.send("Owners have not enabled the commands yet!")
            return False

    @command(name="rightflip", aliases=["sagtakla"])
    async def rightflip(self, ctx):
        if self.isOn:
            await ctx.send("Right Flip")
            return True
        else:
            await ctx.send("Owners have not enabled the commands yet!")
            return False

    @command(name="leftflip", aliases=["soltakla"])
    async def leftflip(self, ctx):
        if self.isOn:
            await ctx.send("Left Flip")
            return True
        else:
            await ctx.send("Owners have not enabled the commands yet!")
            return False

    @command(name="rightspin", aliases=["sagadon"])
    async def rightspin(self, ctx):
        if self.isOn:
            await ctx.send("Right Spin")
            return True
        else:
            await ctx.send("Owners have not enabled the commands yet!")
            return False

    @command(name="leftspin", aliases=["soladon"])
    async def leftspin(self, ctx):
        if self.isOn:
            await ctx.send("Left Spin")
            return True
        else:
            await ctx.send("Owners have not enabled the commands yet!")
            return False

    #######################################################
    #######################################################

    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up("fun")


def setup(bot):
    bot.add_cog(Fun(bot))
