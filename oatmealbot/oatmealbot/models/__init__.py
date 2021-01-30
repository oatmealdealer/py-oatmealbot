from __future__ import annotations
from os import getenv

from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine, EmbeddedModel, Field, Model

mongo_client = AsyncIOMotorClient(getenv("MONGODB_URI"))

ENGINES = {}
ENGINE = None


class ModelExtensions:
    @classmethod
    def get_db(cls, db_name):
        if db_name in ENGINES:
            return ENGINES[db_name]
        else:
            engine = AIOEngine(mongo_client, str(db_name))
            ENGINES[db_name] = engine
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
        collection = "guilds"

    @classmethod
    @property
    def db(self) -> AIOEngine:
        return self.get_db("guilds")

    @classmethod
    async def find_one(cls, guild_id: int) -> Guild:
        return await cls.db.find_one(cls, cls.id == guild_id)

    @classmethod
    async def find(cls, *args, **kwds):
        return await cls.db.find(cls, *args, **kwds)
