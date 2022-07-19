# Third party modules
import discord
import os
import gspread

import service.google_sheets_service as google_sheets_service

from dotenv import load_dotenv

load_dotenv()


class Bot(discord.Client):

    google_service = gspread.service_account("google_credentials/service_account.json")

    async def on_ready(self):
        print("Online - Fiat Lux Bot")
        # print("EXAMPLE_ENVIRONMENT_VARIABLE = " + os.getenv("EXAMPLE_ENVIRONMENT_VARIABLE"))

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
            # Example function
            await do_stuff(message)

        if message.content == "^test_spreadsheet":
            # Example function
            print("testing the spreadsheet")
            return_str = await google_sheets_service.test(self.google_service)
            await message.channel.send(return_str[0] + " and " + return_str[1] + " were the tanks for " + return_str[2])


async def do_stuff(message):
    await message.channel.send("Fiat Lux is doing stuff!")

# Intents are the buckets of events that the discord bot subscribes to
intents = discord.Intents.default()

client = Bot(intents=intents)
client.run(os.getenv("BOT_TOKEN"))
