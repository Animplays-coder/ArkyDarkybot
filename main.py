import discord
from discord.ext import commands
import re
import requests
import random
client = commands.Bot(command_prefix='>')


class MyClient(discord.Client):
    bot = ''
    async def report(self, ctx, user : discord.Member, *reason):
        channel = self.get_channel(786280823397023700) 
        author = ctx.message.author
        rearray = ' '.join(reason[:]) 
        if not rearray: 
           await channel.send(f"{author} has reported {user}, reason: Not provided")
           await ctx.message.delete() 
        else:
           await channel.send(f"{author} has reported {user}, reason: {rearray}")
           await ctx.message.delete()
    
    async def on_ready(self):
        await client.change_presence(status=discord.Status.online, activity=discord.Game('the prefix > | >help'))
        print("Bot is connecting...\n")
        print("Bot is live!")

    async def on_message(self, message):
        print(f"message from {message.author}: {message.content}")

    async def on_member_join(self, member):
        await member.create_dm()
        await member.dm_channel.send(
                f"Hi {member.name}, welcome to Programmer's Cafe :>")
        
    async def youtube(self, ctx, *, arg):
        """Search YouTube"""
        query = str(arg)
        # print("query: ", query)
        url = "https://www.youtube.com/results?search_query="
        with requests.get(url + query) as reponse:
            # regex = '/watch\?v\=[a-zA-z0-9/_/-/*]+'
            regex = '/watch\?v\=(.*?)\\"'
            # regex = r'/watch\?v=[a-zA-Z0-9]+'
            match = re.findall(regex, response.text)[0]
            payload = "https://www.youtube.com/watch?v=" + match
            # print(payload)
            await ctx.send(f"> Here is your result for: {query}\n{payload}")

client = MyClient()
with open('token.txt','r') as my_token:
    token = my_token.read()
client.run(token)
