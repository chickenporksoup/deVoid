import discord
from discord.ext import commands
import CONFIG

class Moderation():
    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context = True)
    async def role(self, cxt, role_name: str):
        allowed_roles = (CONFIG.ROLES)
        try:
            role = discord.utils.get(cxt.message.author.server.roles, name = role_name)
            if role.id in allowed_roles:
                await self.bot.add_roles(cxt.message.author, role)
                await self.bot.say('GG ' + cxt.message.author.name)
            else:
                await self.bot.say("You do not have permission to access that role.")
        except (AttributeError,IndexError):
            await self.bot.say("Err. Please try again. **Hint: Mention the name of an existing role in this server.**")
    
    @commands.command(pass_context = True)
    async def kick(self, cxt, *, member: discord.Member):
        pass


def setup(bot):
    bot.add_cog(Moderation(bot))
