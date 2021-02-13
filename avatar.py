import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='$')

@bot.command()
async def pp(ctx, user:discord.User):
    await ctx.send(user.avatar_url)
    
   
   
bot.run("token")
