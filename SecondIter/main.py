import discord
import os
from replit import db
from Event import Event, modify, delete, addParticipant, removeParticipant, FormattedStr


intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)


#The following function allows the bot to log in. 

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

#The following function allows the bot to respond to messages.

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$NewEvent'):
    NewEventSplit = message.content.split(";")
    MainEvent = Event(NewEventSplit[1],NewEventSplit[2],NewEventSplit[3],NewEventSplit[4],NewEventSplit[5],NewEventSplit[6],NewEventSplit[7])
    FoormattStr = FormattedStr()
    await message.channel.send(FoormattStr)

  if message.content.startswith('$ModifyEvent'):
    ModifyEventSplit = message.content.split(";")
    modify(ModifyEventSplit[2],ModifyEventSplit[3])
    FoormattStr = FormattedStr()
    await message.channel.send(FoormattStr)

  if message.content.startswith('$JoinEvent'):
    JoinEventSplit = message.content.split(";")
    addParticipant(JoinEventSplit[2])
    FoormattStr = FormattedStr()
    await message.channel.send(FoormattStr)

  if message.content.startswith('$LeaveEvent'):
    LeaveEventSplit = message.content.split(";")
    JoinEvent = removeParticipant(LeaveEventSplit[2])
    FoormattStr = FormattedStr()
    await message.channel.send(FoormattStr)

client.run()
#Main_Event = Event("BlueDream", "Come One, Come All for a Blues Harmonica Jam Sesh!",10/9/2024,"80 University Ave W, Waterloo, ON N2L 3C7","Lucky",None)

#Main_Event.addParticipant("Cyro")

#print(Main_Event.Participants)

#Main_Event.removeParticipant("Cyro")

#print(Main_Event.Participants)
