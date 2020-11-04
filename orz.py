import os
import discord
from dotenv import load_dotenv
load_dotenv()
import random
TOKEN = "YOUR TOKEN"
client = discord.Client()
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == 'plz orz':
        response = 'sir how so orz brooo <:liorz:751117138793726082>'
        await message.channel.send(response)
    if message.content == 'plz greet':
        response = 'hiii broooo orzzzz <:liorz:751117138793726082> <:liorz:751117138793726082> <:liorz:751117138793726082>'
        await message.channel.send(response)
    if message.content == 'plz roadmap':
        response = 'bro gimme roadmap brooo plz :pray::pray:'
        await message.channel.send(response)
    if message.content == 'plz check':
        response = 'whats wrong with sol broo????'
        await message.channel.send(response)
    if message.content == 'plz testcase':
        response = 'help broo, give one testcase plzzz??? :pray::pray::pray:'
        await message.channel.send(response)
    if message.content == 'plz job':
        response = 'bro i want job at Goggle brooo plzz'
        await message.channel.send(response)
    if message.content == 'plz halp':
        response = 'broo help in this problemm plzz..this is not from ongoing contest brooooo :pray::pray::pray:'
        await message.channel.send(response)
    if message.content == 'plz help bot':
        response = "```yaml\nCommands with mandatory prefix plz:\norz\ngreet\nroadmap\ntestcase\njob\nhelp\ntrivial\nrequest\ncolin\nhw\nvises\nnishuz\nbro\nkms\nred```"
        await message.channel.send(response)
    if message.content == 'plz trivial':
        response = "plzz do proper bro so trivial broo"
        await message.channel.send(response)
    if message.content == 'plz request':
        response = "plz do brooo plzzz i request u broooo"
        await message.channel.send(response)
    if message.content == 'plz colin':
        response = "plz colin bro plzzz???? :pray:"
        await message.channel.send(response)
    if message.content == 'plz kek':
        response = "broooooo hahahahahahaha <:kekw:764315571163496468>"
        await message.channel.send(response)
    if message.content == 'plz hw':
        response = "do my hw broo plzzzzzzzz <:pklove:751118494090657853>"
        await message.channel.send(response)
    if message.content == 'plz nishuz':
        response = "lol brooo ur so retarded <:kekw:764315571163496468>"
        await message.channel.send(response)
    if message.content == 'plz vises':
        response = "plz give me smart like vishesh broooo :pray:"
        await message.channel.send(response)
    if message.content == 'plz red':
        response = "hii brooo am grey now plz halp.. how to red in 3 months????"
        await message.channel.send(response)
    if message.content == 'plz bro':
        response = "plz brooooo plzzzz plzzz plzzz???? <:ughh:751118102254583848>"
        await message.channel.send(response)
    if message.content == 'plz uBun2':
        response = "plz brooooo plzzzz plzzz plzzz your cf ID???? <:ughh:751118102254583848>"
        await message.channel.send(response)
    if message.content == 'plz antiorz':
        response = "bro plzzz no orz me bro i retard"
        await message.channel.send(response)
    if message.content == 'plz kms':
        response = "galen colinnnnn broooo"
        await message.channel.send(response)
    #if message.content == 'plz IGM':
    #    for orz in range(100):
    #        response = "<@!145266128363585536> IGM <:liorz:751117138793726082> <:liorz:751117138793726082> <:liorz:751117138793726082> <:liorz:751117138793726082> <:liorz:751117138793726082> woohooooo"
    #        await message.channel.send(response)
@client.event
async def on_ready():
     print("Connected!")
client.run(TOKEN)


