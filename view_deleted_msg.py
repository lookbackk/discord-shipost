import discord
from discord.ext import commands





bot = commands.Bot(command_prefix='$', self_bot = True)

@bot.event
async def on_message_delete(message):
    await message.channel.send("Le message : \"{}\" de {} a été supprimé {}".format(message.content, message.author, message.author.avatar_url))
    await bot.process_commands(message)
    
    
    
bot.run("token", bot=False)
