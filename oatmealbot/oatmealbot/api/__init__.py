from fastapi import FastAPI
from oatmealbot.models import Guild

app = FastAPI()


@app.get("/")
async def hello():
    return {"message": "hlelo!"}


@app.get("/guild/{guild_id}")
async def get_guild(guild_id: int):
    return (await Guild.find(guild_id)).dict()
