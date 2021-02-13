import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='$', self_bot = True)

@bot.command()
async def bordel(ctx):
    users = bot.users
    for user in users:
        await ctx.send(user.avatar_url)
        
bot.run("token", bot=False)
