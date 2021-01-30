from typing import List

import discord
from oatmealbot.models import AIOEngine, Guild


async def dump_guild(guild: discord.Guild):
    # db = mongo_client[str(guild.id)]
    # guild_col: motor.AsyncIOMotorCollection = db.guild
    # find_guild = await guild_col.find_one({"id": guild.id})
    # if find_guild is None:
    insert_guild = Guild(name=guild.name, id=guild.id)
    await insert_guild.save()

    print("Inserted guild: {}".format(guild))


class OatClient(discord.Client):
    # @client.event
    async def on_ready(self):
        print("We have logged in as {0.user}".format(self))
        print("Connected guilds: {0.guilds}".format(self))
        for guild in self.guilds:
            # print(dict_from_obj(guild, ["id", "name"]))
            await dump_guild(guild)

    # @client.event
    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("!ping"):
            await message.channel.send("pong!")


client = OatClient()
