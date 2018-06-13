from discord.ext import commands


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

def setup(bot):
    bot.add_cog(Jakestest(bot))
