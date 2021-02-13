import discord
from discord.ext import commands





bot = commands.Bot(command_prefix='$', self_bot = True)


@bot.event
async def on_message(message):
    if message.content.startswith(""):
        guild = discord.utils.get(bot.guilds, name="NewbieContest")
        emoji = discord.utils.get(guild.emojis, name="rm")
        await message.add_reaction(emoji)
    
    
    
bot.run("token", bot=False)

# delete bot=False and self_bot = True for bot
