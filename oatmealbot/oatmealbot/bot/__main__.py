from os import getenv
from .client import client

# from os.path import dirname
# from dotenv import load_dotenv
# load_dotenv(dirname(__file__) + "/../.env")


client.run(getenv("BOT_TOKEN"))
