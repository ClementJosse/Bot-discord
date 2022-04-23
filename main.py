import discord
import os
import logging
from discord import Client
from argparse import ArgumentParser
from argparse import Namespace
from dotenv import load_dotenv
import json

class MyBot(Client):
    def __init__(self):
        super().__init__()

    async def on_ready(self):
            print("le bot est ready")

    async def on_message(self, message):
        if message.content.lower() == "!ping":
            logging.info(f"<{message.author.name}> : {message.content}")
            await message.channel.send("pong")

        if message.content.lower() == "!help":
            logging.info(f"<{message.author.name}> : {message.content}")
            await message.channel.send("Commandes disponibles: \n !ping => pong")


    async def on_member_join(member):
        general_channel = client.get_channel(584075715167649793)
        general_channel.send(f"Bienvenu à {member.display_name}")


def parse_args() -> Namespace:
    parser = ArgumentParser()
    parser.add_argument("-c", "--config", help="Config file", required = True, dest="config")
    return parser.parse_args()

def setup_log():
    logging.basicConfig(filename='log.log', level=logging.INFO)

load_dotenv(dotenv_path="config")

setup_log()

config = json.load(open(args.config))
bot = MyBot(config)
bot.run(str(config('token')))
