import random
import discord
import os
from discord.ext import commands
import textwrap
import urllib
import aiohttp
import datetime
import json
import requests

client = commands.Bot(command_prefix='#')
client.remove_command("help")



moderationwords = []


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))
  
  
@client.command(description="")
async def ly(ctx, *, search=None):
        try:
            search_url = None
            if search != None:
                search = search.replace(' ', '_')

                search_url = f"https://some-random-api.ml/lyrics?title={search}"
               
            else:
                await ctx.send("``Bruh``")

            async with aiohttp.ClientSession() as cs:
                async with cs.get(search_url) as r:
                    res = await r.json()
                    embed = discord.Embed(title=res["title"],description=res["lyrics"])
                    embed.set_image(url=res["thumbnail"]["genius"])

                    await ctx.send(embed = embed)
                    


        except :
            await ctx.send(f"``There is no page called {search}``")

 
@client.command()
async def coolrate(ctx):
    myEmbedCoolRate = discord.Embed(title="CoolRate", description = f"You are {random.randrange(101)}% cool {ctx.message.author.mention}", color = discord.Colour.random())
    await ctx.send(embed = myEmbedCoolRate)
    
  
@client.command()
async def gayrate(ctx):
  myEmbedGayRate = discord.Embed(title="Gayrate", description = f"You are {random.randrange(101)}% gay {ctx.message.author.mention}", color = discord.Colour.random())
  await ctx.send(embed = myEmbedGayRate)


  
@client.event
async def on_message(message):

  
  if message.content.startswith('hello'):
    await message.channel.send('Hello!')
  await client.process_commands(message) 
    
  for word in moderationwords:
    if word in message.content:
      await message.delete()  

    
  
  if message.content.startswith("#version"):
      myEmbedVersion = discord.Embed(title="Current Version", description="The bot is on version Alpha", color=0x00ff00)
      myEmbedVersion.add_field(name="Version Code:",value="Alpha", inline=False)
      myEmbedVersion.add_field(name="Date Released:",value="Not released yet.", inline=False)
      await message.channel.send(embed=myEmbedVersion)
      
  if message.content.startswith("#help"):
    myEmbedhelp = discord.Embed(title="Help menu", description="", color=0x00ff00)
    myEmbedhelp.add_field(name="general",value="#help : Help menu (this). \n #version : See what version the bot is on!", inline=False)
    myEmbedhelp.add_field(name="Fun",value="#coolrate : Do you want to know how cool you are? Use this command! \n #gayrate : The bot knows if you are gay or not. Use this command. \n #ly <yoursong> : to get the lyrics of a song n\MORE COMING SOON!", inline=False)
    await message.channel.send(embed=myEmbedhelp)   
    

client.run("TOKEN")
