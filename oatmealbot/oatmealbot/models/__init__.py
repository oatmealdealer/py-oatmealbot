from __future__ import annotations
from os import getenv

from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine, EmbeddedModel, Field, Model

mongo_client = AsyncIOMotorClient(getenv("MONGODB_URI"))

ENGINES = {}
ENGINE = None


class ModelExtensions:
    @classmethod
    def get_db(cls, guild_id: int):
        if guild_id in ENGINES:
            return ENGINES[guild_id]
        else:
            engine = AIOEngine(mongo_client, str(guild_id))
            ENGINES[guild_id] = engine
            return engine

    @property
    def db(self) -> AIOEngine:
        return self.get_db(self.guild_id())

    async def save(self):
        await self.db.save(self)

    def guild_id(self):
        raise NotImplementedError


class Guild(Model, ModelExtensions):
    id: int = Field(primary_field=True)
    name: str

    class Config:
        collection = "guild"

    def guild_id(self):
        return self.id

    @classmethod
    async def find(cls, guild_id: int) -> Guild:
        return await cls.get_db(guild_id).find_one(cls, cls.id == guild_id)
