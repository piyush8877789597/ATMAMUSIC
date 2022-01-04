import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

load_dotenv()
que = {}
admins = {}

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ARQ_API_KEY = getenv("ARQ_API_KEY")
BOT_TOKEN = getenv("BOT_TOKEN")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
SESSION_NAME = getenv("SESSION_NAME", "session")
YOUR_NAME = getenv("https://telegra.ph/file/f48b99702ca1e882e9dda.jpg")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5043873192").split()))
aiohttpsession = aiohttp.ClientSession()
