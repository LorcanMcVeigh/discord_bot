from discord import Game
from discord.ext.commands import Bot

BOT_PREFIX = "?"
TOKEN = ""

client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name="your emotions"))
    print("Logged in as " + client.user.name)

@client.command(name='greet',
                description='greets the person who mention the bot',)
async def greet(context):
    await client.say("Hello " + context.message.author.mention, + ":wave:")

@client.command(name='changeWord', description='capitalises every second letter')
async def changeWord(ctx, arg)
    newword = ""
    count = 0
    for w in arg:
        if count % 2 != 0:
            newword += w.upper()
        else:
            newword += w 
        count += 1
    await ctx.send(newword)