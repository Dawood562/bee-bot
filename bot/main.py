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
from datetime import datetime
from jsonfuncs import *

intents = discord.Intents.default()
client = commands.Bot(command_prefix = 'bee', help_command=None, intents=intents, allowed_mentions = discord.AllowedMentions(everyone = False, roles = False), strip_after_prefix=True, case_insensitive=True, activity=discord.Activity(type=discord.ActivityType.watching, name='🐝'))


def numbering(bees):
    if bees == 1:
        return "1 bee"
    else:
        if bees % 1 == 0:
            return f"{int(bees)} bees"
        else:
            return f"{bees} bees"




# Set variables to be used throughout the bot's lifetime
beeids = [363013743128608771, 221188745414574080, 830217318054887424]
beeemoji="🐝"



def is_a_bee():
    async def wrap_function(ctx):
        if ctx.author.id in beeids:
            return True
        else:
            return False
    return commands.check(wrap_function)


# Event for when the bot is ready
@client.event
async def on_ready():
    print(f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}::: Bot is ready!')


# Error handling
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send(f'**Missing Arguments in {ctx.command}.**\nIf you need help with a command, use `bee help`.')
    else:
        print('Ignoring exception in command {}:'.format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)


@client.command()
@is_a_bee()
async def add(ctx, bees, msgid: int=None):
    try:
        bees = float(bees)
    except:
        msg = "You need to specify a valid number of bees."
    else:
        if bees % 0.5 != 0:
            msg = "You need to specify a valid number of bees."
        elif (msgid is None) and (ctx.message.reference is None):
            msg = "You need to reply to a message (or provide a message ID) to check how many bees it has!"
        elif msgid is None:
            msgid = ctx.message.reference.message_id
            add_bees(msgid, bees)
            vw = view_bees(msgid)
            if bees > 0:
                msg = f"Successfully added {numbering(bees)} to the message! It now has {numbering(vw)}."
            elif bees <0:
                msg = f"Successfully removed {numbering(abs(bees))} from the message! It now has {numbering(vw)}."
    await ctx.reply(msg, mention_author=False)


@client.command()
async def bees(ctx, msgid: int=None):
    if (msgid is None) and (ctx.message.reference is None):
        msg = "You need to reply to a message (or provide a message ID) to check how many bees it has!"
    elif msgid is None:
        msgid = ctx.message.reference.message_id
        vw = view_bees(msgid)
        if vw == 1:
            msg = f"This message has 1 bee."
        else:
            if vw % 1 == 0:
                msg = f"This message has {int(vw)} bees."
            else:
                msg = f"This message has {vw} bees."        
    await ctx.reply(msg, mention_author=False)

@client.command()
async def explain(ctx):
    emb = discord.Embed(title="BEE BEE BEE BEE BEE BEE BEE BEE", description="I add bees to messages\nOnly the Bee Master Himself (<@363013743128608771>) can add bees to messages with `bee add <amount>` when replying to a message.\nThe rest of you worker bees can view how many bees a message has by using `bee bees` when replying to a message.\nFinally, if you forget about these commands then you can use `bee explain` to get this message again.", color=0xc27c0e)
    emb.set_footer(text = "Happy bee-ing!", icon_url="https://imgur.com/kgW4wlc.png")
    await ctx.reply(mention_author=False, embed=emb)



@client.event
async def on_raw_reaction_add(payload):
    if payload.emoji.name == beeemoji:
        add_bees(payload.message_id, 1)

@client.event
async def on_raw_reaction_remove(payload):
    if payload.emoji.name == beeemoji:
        add_bees(payload.message_id, -1)


# Start the bot
client.run(os.environ.get("TOKEN"))
