from typing import List
import discord

from motor.motor_asyncio import AsyncIOMotorClient
import motor.motor_asyncio as motor
from os import getenv
from models import Guild, AIOEngine

# client = discord.Client()
mongo_client = AsyncIOMotorClient(getenv("MONGODB_URI"))
engine = AIOEngine(mongo_client)
# db = mongo_client.admin


def dict_from_obj(thing, attrs: List[str]):
    return {slot: getattr(thing, slot) for slot in attrs}


async def dump_guild(guild: discord.Guild):
    # db = mongo_client[str(guild.id)]
    # guild_col: motor.AsyncIOMotorCollection = db.guild
    # find_guild = await guild_col.find_one({"id": guild.id})
    # if find_guild is None:
    insert_guild = Guild(id=guild.id, name=guild.name)
    await engine.save(insert_guild)
    print("Inserted guild {0.id}: {}".format(guild, insert_guild))


class OatClient(discord.Client):
    # @client.event
    async def on_ready(self):
        print("We have logged in as {0.user}".format(self))
        print("Connected guilds: {0.guilds}".format(self))
        for guild in self.guilds:
            print(dict_from_obj(guild, ["id", "name"]))
            await dump_guild(guild)

    # @client.event
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("!ping"):
            await message.channel.send("pong!")


client = OatClient()
