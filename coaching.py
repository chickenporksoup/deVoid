import discord
from discord.ext import commands
import CONFIG
import json, os.path


class Coaching():
    def __init__(self,bot):
        self.bot = bot
    
    @commands.command(pass_context = True)
    async def coach(self, cxt, IGN: str):
        allowed_roles = (CONFIG.ROLES)
        key_val = str(cxt.message.author.name)
        role = discord.utils.get(cxt.message.author.server.roles, name = 'Back Benchers')    
        await self.bot.add_roles(cxt.message.author, role)
        await self.bot.say('GG {}! Your IGN has been enrolled for coaching'.format(cxt.message.author.name))
        if os.path.isfile('members.json'):
            with open('members.json','r') as f:
                coaching = json.load(f)
        coaching.update({ key_val : {} })
        coaching[key_val]['IGN'] = IGN
        coaching[key_val]['Coaching'] = True
        with open('members.json','w') as f:
            json.dump(coaching, f, indent=2)


    @commands.command(pass_context = True)
    async def view_students(self, cxt):
        coaching, stud_list = {}, ""
        try:
            with open('members.json','r') as f:
                coaching = json.load(f)
        except Exception:
            await self.bot.say('Err, there was an error, locating the file. Please try again!')
        for i in coaching:
            if coaching[i]['Coaching'] == True:
                stud_list += coaching[i]['IGN'] + "\n"
        await self.bot.say(stud_list)
                
            

def setup(bot):
    bot.add_cog(Coaching(bot))
