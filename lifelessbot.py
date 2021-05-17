import discord
import os
import requests
import json
import youtube_dl
import datetime
from discord.ext import commands
from discord.utils import get
from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from pytube import YouTube
#from youtube_search import YoutubeSearch
from youtubesearchpython import VideosSearch

client=discord.Client()
lifelessemoji='<a:lifeless:843039789405044757>'
mycandy='<:mycandy:843491792279961601>'
balbasaur='<:balbasaur:843491791658549258>'
pinkheart='<:pinkheart:843491791553953804>'
girlkiss='<a:girlkiss:843491799246962708>'
girlagree='<a:girlagree:843491797443412038>'
discogirl='<a:discogirl:843491796838252595>'
cute='<a:cute:843491796347912242>'
hoodie='<a:lifelesshoodie:843491795245334578>'

@client.event
#async def on_ready():
  #activity = discord.Activity(type=discord.ActivityType.listening, name="The Sweetness of Lifeless")
  #await client.change_presence(status=discord.Status.idle, activity=activity)
  #print('We have logged in as {0.user}'.format(client))

# Interactive Part of LifelessBot

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('lifelessHello'):
    await message.channel.send('Hello, Hello, Hello! This is LifelessBot reciprocating the Sweetness of Lifeless. :heart:')

  if message.content.startswith('lifelessKick'):
    await message.channel.send('Sorry! Lifeless is too sweet to kick/ban sweet people! <a:cutecat:842966553321275412>')

  if message.content.startswith('lifelessBan'):
    await message.channel.send('Sorry! Lifeless is too sweet to kick/ban sweet people! <a:cutecat:842966553321275412>')

  if message.content.startswith('lifelessInspire'):
    quote=get_quote()
    await message.channel.send('_Here is an inspirational quote from the sweetness factory of Lifeless_ :heart:'+'\n'+'\n'+quote)

  if message.content.startswith('lifelessSowiee'):
    quote=get_quote()
    await message.channel.send('<:Sowiee:837558958071611412>')

  if message.content.startswith('lifelessCutecat'):
    quote=get_quote()
    await message.channel.send('<a:cutecat:842966553321275412>')

  if message.content.startswith('lifelessAstonished'):
    quote=get_quote()
    await message.channel.send('<:OhhAisa:837558942262493195>')

  if message.content.startswith('lifelessInnocent'):
    quote=get_quote()
    await message.channel.send('<:Innocent:837676007779467325>')

  if message.content.endswith('lifelessCute'):
    quote=get_quote()
    await message.channel.send('<a:cutegirl:842992585378103296>')

  if message.content.startswith('Hi Lifeless!'):
    quote=get_quote()
    await message.channel.send(lifelessemoji+lifelessemoji+lifelessemoji)

 #Music Part of LifelessBot

client1=commands.Bot(command_prefix='lifeless')
def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " \n" +"- "+ json_data[0]['a']
  return(quote)
@client1.event
async def on_ready():
  activity = discord.Activity(type=discord.ActivityType.listening, name="The Sweetness of Lifeless")
  await client1.change_presence(status=discord.Status.idle, activity=activity)
  print('We have logged in as {0.user}'.format(client1))

@client1.command()
async def Cute(ctx):
  await ctx.send('<a:cutegirl:842992585378103296>')
@client1.command()
async def Hello(ctx):
  await ctx.send('Hello, Hello, Hello! This is LifelessBot reciprocating the Sweetness of Lifeless. :heart:')
@client1.command()
async def Kick(ctx):
  await ctx.send('Sorry! Lifeless is too sweet to kick/ban sweet people! <a:cutecat:842966553321275412>')
@client1.command()
async def Ban(ctx):
  await ctx.send('Sorry! Lifeless is too sweet to kick/ban sweet people! <a:cutecat:842966553321275412>')
@client1.command()
async def Inspire(ctx):
  quote=get_quote()
  await ctx.send('_Here is an inspirational quote from the sweetness factory of Lifeless_ :heart:'+'\n'+'\n'+quote)
@client1.command()
async def Sowiee(ctx):
  await ctx.send('<:Sowiee:837558958071611412>')
@client1.command()
async def Cutecat(ctx):
  await ctx.send('<a:cutecat:842966553321275412>')
@client1.command()
async def Vibe(ctx):
  await ctx.send(lifelessemoji+lifelessemoji+lifelessemoji)
@client1.command()
async def Emotes(ctx):
  await ctx.send("_Here are the favourite emotes of Lifeless_"+'\n'+lifelessemoji+mycandy+balbasaur+girlkiss+girlagree+pinkheart+discogirl+cute+hoodie+'<a:cutecat:842966553321275412>')
@client1.command()
async def WishBirthdayChoti(ctx):
    await ctx.send("Happy birthday <@759116563159711814>! Missing you a lotttttttttttttttttttttttttttttttttttttttttttttt! Lots, lots and lots of loveeee for you... "+girlkiss+"-Opti Bhaiyya")
@client1.command(pass_context=True)
async def Connect(ctx):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client1.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
@client1.command(pass_context=True)
async def Disconnect(ctx):
    if ctx.message.author.voice:
        channel = ctx.message.author.voice.channel
        server = ctx.message.guild.voice_client
        await server.disconnect()


@client1.command(pass_context=True)
async def join(ctx):
  channel=ctx.message.author.voice.voice_channel
  await client1.join_voice_channel(channel)

  LIFELESSTOKEN='ODQyOTM5MjExNTA5OTIzODYy.YJ8mUQ.JR73ff4u4cdi4eXWcb3SH00MDo8'
#my_secret = os.environ['LIFELESSTOKEN']

#Start of youtube_dl
players = {}

@client1.command(pass_context=True)
async def play(ctx, search):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client1.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    guild = ctx.message.guild
    voice_client = guild.voice_client
    player = await voice_client.create_ytdl_player(video)
    players[server.id] = player
    player.start()

@client1.command()
async def Play(ctx, url : str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Please wait for the current playing music to end or use the 'lifelessStop' command. Love Love <a:cutegirl:842992585378103296>")
        return

    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(client1.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    #voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': '249',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    await ctx.send("Let's vibe with the song!"+lifelessemoji)

@client1.command()
async def Stop(ctx):

    voice = get(client1.voice_clients, guild=ctx.guild)
    voice.stop()
    await ctx.send('I guess you cannot hear the sweetness anymore.<a:cutecat:842966553321275412>')


#EVENT ORGANIZATION

@client1.command()
async def DM(ctx, user: discord.User, *, message=None):
    message = message or "EVENT-1 '\n'Hello Hello <a:girlkiss:843491799246962708> '\n'Type **lifelessParticipate** to participate. "
    await user.send(message)
    
event_1_usernames_list=[]

@client1.command()
async def Participate(ctx):
    await ctx.send(f'Hi {ctx.author.mention}, thanks for your participation. Looking forward to your performance! {lifelessemoji}')
    event_1_usernames_list.append(ctx.message.author.display_name)

@client1.command()
async def ListEvent1(ctx):
    await ctx.send('This is the list of participants : {}'.format(', '.join(event_1_usernames_list)))











#EDIT1
#client.run(LIFELESSTOKEN)
client1.run('ODQyOTM5MjExNTA5OTIzODYy.YJ8mUQ.68ae5ztqsxc8aEg2_MHhvATsmNk')
