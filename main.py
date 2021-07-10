#!/usr/bin/env python
"""
A basic bot to emulate plugin reviews by a certain person
set your dicord token to the env variable 'DISCORD_TOKEN'
"""

import os
import sys
import random
import argparse
import discord

STARTS = [
    "I’m really impressed by",
    "I'm blown away by",
    "I'm stunned by",
    "I'm shocked by",
    "I'm amazed by"
]

MIDS = [
    "how much animation",
    "the new avenues",
    "the epic farts"
]

ENDS = [
    "gives me!",
    "is opening!",
    "adds."
]

def get_token():
    """
    The token either exists as an argument or as an env variable
    This gets from either
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("token", nargs="?", const="bullshit")
    args = parser.parse_args()
    if args.token != "bullshit":
        return args.token
    if os.environ.get("DISCORD_TOKEN"):
        return os.environ["DISCORD_TOKEN"]
    print("No discord token found. You need to either:")
    print("  > Run this script with the token as an argument")
    print("  > set the DISCORD_TOKEN env variable")
    sys.exit(1)

async def generate_message(plugin):
    """
    Take the above list and choose randomly to generate the message
    """
    start = random.choice(STARTS)
    mid = random.choice(MIDS)
    end = random.choice(ENDS)
    return f"{start} {mid} {plugin} {end}"


class Richard(discord.Client):
    """extension of the discord client to allow messages"""
    async def on_ready(self):
        """make sure it's alive"""
        print("Logged on as {0}!".format(self.user))

    async def on_message(self, message):
        """respond when appropriate"""
        if message.author.id == self.user.id:
            return
        if message.content.startswith("!devine"):
            plugin = ' '.join(message.content.split()[1:])
            await message.reply(await generate_message(plugin))

if __name__ == "__main__":
    client = Richard()
    token = get_token()
    client.run(token)
