import discord
import MeCab
import yaml
from datetime import datetime

with open('config.yml') as file:
    object = yaml.safe_load(file)
    TOKEN = object['TOKEN']
    CHANNELID = object['CHANNELID']

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if not message.author.bot:
        if message.content == "in":
            moment = datetime.now().strftime('%H:%M')
            global in_time
            in_time = int(moment[0:2])
            channel = client.get_channel(CHANNELID)
            await channel.send("Have fun at work! The current time is {}. When you leave work, please say 'out' on this channel".format(moment))

        elif message.content == "out":
            moment = datetime.now().strftime('%H:%M')
            global out_time
            out_time = int(moment[0:2])
            working = out_time-in_time
            channel = client.get_channel(CHANNELID)
            wage = 1000
            await channel.send("Take a good rest!! The current time is {}.".format(moment))
            await channel.send("Today's work time is {} hour.".format(working))
            await channel.send("Today's wage is {} yen".format(working*wage))

        elif message.content == "help":
            await channel.send("Is there anything that I can help you with this time?\nHelp with attendance record.\nPlease say 'in' on this channel when you go to work")

client.run(TOKEN)





client.run(TOKEN)
