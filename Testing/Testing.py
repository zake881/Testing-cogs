import discord
from discord.ext import commands
import time
from __main__ import send_cmd_help

class Jakestest:
    """Dis mine!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def Jake1(self, ctx):
        """This is Jakes way of slowly learning kek"""
        await self.bot.say("Jab you suck dick")
    @commands.command(pass_context=True)
    async def Jake2(self, ctx):
        """This is Jakes way of slowly learning kek"""
        await self.bot.say("this is all it is")
        

    @commands.command(pass_context=True)
    async def ping(self,ctx):
        """pseudo-ping time"""
        channel = ctx.message.channel
        t1 = time.perf_counter()
        await self.bot.send_typing(channel)
        t2 = time.perf_counter()
        await self.bot.say("pseudo-ping: {}ms".format(round((t2-t1)*1000)))

    
def setup(bot):
    bot.add_cog(Jakestest(bot))
