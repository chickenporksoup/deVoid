import discord
from discord.ext import commands
from datetime import datetime
from pytz import timezone
import CONFIG

poll, poll_msg, op, options = False, "", {}, []
q, total, voted = "", 0, set()

class Poll():
    def __init__(self,bot):
        self.bot = bot    

    @commands.command(pass_context = True)
    async def poll(self,cxt):
        global poll_msg, poll, op, options, q, total
        if poll == True:
            await self.bot.say('A poll is already running at the moment. Please stop the previous poll to start a new one')
        else:
            query = cxt.message.content.split("<")[0].strip().strip("-poll")
            options = cxt.message.content.split("<")[1].strip(">").split()
            q = query
            total, count = 0, 0
            for i in options:
                op[i] = 0
            msg = "**" + query + "**\n"
            for i in options:
                msg += "{} - {} votes\t\t".format(i, op[i])
                count += 1
                if count%3 == 0:
                    msg += "\n"
            msg += "\n**To vote, please go to the <#420780429721731082> channel and type -poll_vote <your choice>\neg: -poll_vote yes*"
            poll_msg = await self.bot.send_message(discord.Object(id = CONFIG.POLL), msg)
            await self.bot.send_message(discord.Object(id = '418836247310630922'),'@here A poll has been created!\n**TOPIC: {}**'.format(q))
            poll = True    
    

    @commands.command(pass_context = True)
    async def poll_vote(self, cxt, choice:str = ""):
        if poll == True:
            global poll_msg, op, options_given, options, total, voted
            if cxt.message.author.id in voted:
                await self.bot.say('Errm, your vote has already been recorded. YOU CHEAT!')
            else:
                try:
                    op[choice] += 1
                    total += 1
                    voted.add(cxt.message.author.id)
                    msg = "**" + q + "**\n"
                    for i in options:
                        msg += "{}-{} votes ({}%)\t\t".format(i, op[i], round((op[i]/total)*100))
                    msg += "\n\n**To vote, please go to the <#420780429721731082> channel and type -poll_vote <your choice>\neg: -poll_vote yes*"
                    await self.bot.edit_message(poll_msg, msg)
                except Exception:
                    await self.bot.say('Please provide a valid argument')


    @commands.command(pass_context = True)
    async def poll_stop(self,cxt):
        global poll_msg, poll, total, q, op, voted
        poll_msg, poll, total, op = "", False, 0, {}
        voted.clear()
        await self.bot.send_message(discord.Object(id = '418836247310630922'),'The current poll has been stopped.\n**TOPIC: {}**'.format(q))
        q = ""



def setup(bot):
    bot.add_cog(Poll(bot))
