# Import all required libraries/functions
import asyncio
import discord
import os
from discord.embeds import Embed
from discord.ext import commands
from discord.ext.commands import errors
from discord.message import Message
import traceback
import sys




intents = discord.Intents.default()
intents.members = True
intents.reactions = True
client = commands.Bot(command_prefix = 'bee', help_command=None, intents=intents, allowed_mentions = discord.AllowedMentions(everyone = False, roles = False), strip_after_prefix=True, case_insensitive=True, activity=discord.Activity(type=discord.ActivityType.watching, name='🐝'))

# Set variables to be used throughout the bot's lifetime (list below is the order in which the embed colours appear; one for each member)
beeids = [363013743128608771, 221188745414574080]


# Event for when the bot is ready
@client.event
async def on_ready():
    print(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}::: Bot is ready!')


# Error handling
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'**Missing Arguments in {ctx.command}.**\nIf you need help with a command, use `bee help`.'))
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


@client.command()
@commands.is_owner()
async def view(ctx):
    ctx.reply("ayo mr white")
    ctx.reply(f"{ctx}")

# Start the bot
client_token = os.environ.get("TOKEN")
client.run(client_token)
