from fastapi import FastAPI
from oatmealbot.models import Guild

app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "henlo!"}


@app.get("/guild/{guild_id}")
async def get_guild(guild_id: int):
    return await Guild.find_one(guild_id)


@app.get("/guilds")
async def list_guilds():
    return await Guild.find()
