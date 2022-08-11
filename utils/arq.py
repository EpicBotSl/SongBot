from aiohttp import ClientSession
from motor.motor_asyncio import AsyncIOMotorClient as MongoClient
from pyrogram import Client
from pyrogram.types import Message
from pyromod import listen
from Python_ARQ import ARQ

ARQ_API_URL = "https://thearq.tech"

ARQ_API_KEY = "JRBVAR-JICHKN-DFLDNX-NPRGCH-ARQ"


aiohttpsession = ClientSession()

arq = ARQ(ARQ_API_URL, ARQ_API_KEY, aiohttpsession)
