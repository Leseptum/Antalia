import discord, gamelogic as gl

#Load Data

#Discord Bot
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    game = discord.Game("Atmen")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$'):
        await message.channel.send(gl.getText(message))


#RUN BOT
client.run('OTk3ODg0OTI5MDI5NDYwMDcy.GO-K9j.B6WHWx44xVG5sOqoVVvYCOCbsgfT8qe97xAw_0')

