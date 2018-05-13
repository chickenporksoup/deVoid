import discord
from discord.ext import commands
import CONFIG as config


startup_extensions = ["moderation","poll","suggestions","coaching"]

bot = commands.Bot(command_prefix='-')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    


@bot.event
async def on_member_join(member: discord.Member):
    role = discord.utils.get(member.server.roles, name = "Munions")
    await bot.add_roles(member,role)
    target_member = await bot.get_user_info(str(member.id))
    await bot.send_message(discord.Object(id = "417192065408040960"), "Hey, {}! Welcome to the {}, we hope you enjoy your stay. :grin:".format(member.mention, member.server))
    ##await bot.send_message(target_member, "RULES")


@bot.command()
@commands.has_role('Black Claw')
async def load(extension_name : str):
    """Loads an extension."""
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await bot.say("```py\n{}: {}\n```".format(type(e).__name__, str(e)))
        return
    await bot.say("{} loaded.".format(extension_name))


@bot.command()
@commands.has_role('Black Claw')
async def unload(extension_name : str):
    """Unloads an extension."""
    bot.unload_extension(extension_name)
    await bot.say("{} unloaded.".format(extension_name))


if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))

bot.run(config.token)
