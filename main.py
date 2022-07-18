# Third party modules
import asyncio
import discord
import os

from dotenv import load_dotenv

load_dotenv()


class Bot(discord.Client):

    async def on_ready(self):
        print("Online - Fiat Lux Bot")
        print("EXAMPLE_ENVIRONMENT_VARIABLE = " + os.getenv("EXAMPLE_ENVIRONMENT_VARIABLE"))

    async def on_raw_reaction_add(self, payload):
        if payload.user_id == self.user.id:
            return

    # do something on a reaction

    async def on_message(self, message):
        split_message = message.content.split(" ")
        #        print(split_message)

        # General commands handler
        channel = message.channel
        guild = message.guild

        if message.content == "^example_command":
            # Example function (take out return when uncommenting function)
            # await stuff.do_stuff()
            return

        if message.content == "^another_example_command":
            # Example function (take out return when uncommenting function)
            # await stuff.do_lots_of_stuff()
            return


# Intents are the buckets of events that the discord bot subscribes to
intents = discord.Intents.default()

client = Bot(intents=intents)
client.run(os.getenv("BOT_TOKEN"))
