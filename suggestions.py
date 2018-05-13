import discord
from discord.ext import commands
import CONFIG

class Suggestions():
    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def suggest(self, cxt):
        author = cxt.message.author.name
        await self.bot.send_message(discord.Object(id="415535370646847498"), cxt.message.content.strip("-suggest ")   +"\n - " + author)


def setup(bot):
    bot.add_cog(Suggestions(bot))
