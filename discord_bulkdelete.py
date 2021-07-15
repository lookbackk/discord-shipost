@bot.event
async def on_ready():
    channel = bot.get_channel(channel_id)
    number = 8000000000000
    number=int(number)
    #date = datetime.datetime(year,month, day)
    counter = 0

    async for msg in channel.history(limit=number, before=date):
        if counter < number:
            if msg.author.id == your_id:
                await msg.delete()
                counter+=1
                await asyncio.sleep(0.7)
bot.run("TOKEN", bot=False)
