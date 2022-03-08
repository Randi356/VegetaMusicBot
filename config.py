import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "RendyProjects")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/5b1412cf1b4b3cf1ce5bb.png")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "CutesLucky")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "VegetaSupports")
PROJECT_NAME = getenv("PROJECT_NAME", "VEGETA MUSIC")
OWNER = getenv("OWNER", "@rencprx")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/Randi356/VegetaMusicBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "7"))
PMPERMIT = getenv("PMPERMIT", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
VEGETA = getenv("VEGETA", "https://telegra.ph/file/5b1412cf1b4b3cf1ce5bb.png")
