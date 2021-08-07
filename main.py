import datetime
import string
import time

import discord
from discord import channel


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return
        cmd = message.content.split(" ")
        if message.content.startswith('$'):
            if cmd[0] == '$help':
                if client.get_channel(873284900801896479) == message.channel:
                    embed=discord.Embed(title="ByteSender Help", description="Here's what you asked for!", color=discord.Color.blurple())
                    embed.add_field(name="Commands", value="```$help (Returns this)``` ```$repo (Returns the Repository URL)``` ```$download (Returns the Download URL)``` ```$developer (Returns the Developers)```")
                    embed.add_field(name="Utils", value="```$id (Returns the User ID of you)```")
                    embed.timestamp = datetime.datetime.utcnow()
                    #embed.set_footer(text="\u200b")
                    await message.channel.send(embed=embed)
                else:
                    await message.channel.send("**(!)** This is not the Commands channel. Please execute **" + message.content + "** in the <#873284900801896479> channel and try again.", delete_after=10)
            elif cmd[0] == "$id":
                if client.get_channel(873284900801896479) == message.channel:
                    await message.delete()
                    await message.channel.send("Your ID is **{}**".format(message.author.id), delete_after=30)
                else:
                    await message.channel.send("**(!)** This is not the Commands channel. Please execute **" + message.content + "** in the <#873284900801896479> channel and try again.",delete_after=10)
            elif cmd[0] == '$repo':
                if client.get_channel(873284900801896479) == message.channel:
                    embed = discord.Embed(title="ByteSender Repository", description="Here's what you asked for!", color=discord.Color.blurple())
                    embed.timestamp = datetime.datetime.utcnow()
                    embed.add_field(name="Repository", value="Click [here](https://github.com/RemoteException-Dev/ByteSender) for the Repository URL")
                    #embed.set_footer(text="\u200b")
                    await message.channel.send(embed=embed)
                else:
                    await message.channel.send("**(!)** This is not the Commands channel. Please execute **" + message.content + "** in the <#873284900801896479> channel and try again.",delete_after=10)



client = MyClient()
client.run('token')
