"""
A basic bot to emulate plugin reviews by a certain person
set your dicord token to the env variable 'DISCORD_TOKEN'
"""

import os
import random
import discord

STARTS = [
    "I’m really impressed by",
    "I'm blown away by",
    "I'm stunned by"
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
    try:
        client.run(os.environ["DISCORD_TOKEN"])
    except KeyError:
        print("You forgot to set the DISCORD_TOKEN env variable didn't you, you soft bastard")
