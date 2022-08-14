import re
from datetime import datetime
import asyncio
import os
import time
from config import *
from epic import *
from epic import bot
from pyrogram import *
from pyrogram.types import *
from pyrogram import filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message
from urllib.request import urlretrieve
import requests as r
import wget


def get_text(message: Message) -> [None, str]:
    """Extract Text From Commands"""
    text_to_return = message.text
    if message.text is None:
        return None
    if " " in text_to_return:
        try:
            return message.text.split(None, 1)[1]
        except IndexError:
            return None
    else:
        return None

@bot.on_message(filters.command("saavn"))
async def savnana(client: Client, message: Message):
    song = get_text(message)
    if not song:
        return await message.reply("**searching on saavn 🔎**")
    hmm = time.time()
    lol = await message.edit_text("**📤 downloading....**")
    sung = song.replace(" ", "%20")
    url = f"https://jostapi.herokuapp.com/saavn?query={sung}"
    try:
        k = (r.get(url)).json()[0]
    except IndexError:
        return await eod(lol, "__🥺 song not found baby__")
    title = k["song"]
    urrl = k["media_url"]
    img = k["image"]
    duration = k["duration"]
    singers = k["singers"]
    urlretrieve(urrl, title + ".mp3")
    urlretrieve(img, title + ".jpg")
    file= wget.download(urrl)
    await client.send_audio(message.chat.id,file,caption=f"💞Song name=**{title}**\n ✨Singers=||{singers}||\n ***on saavn**" )   
    await lol.delete()
    os.remove(title + ".mp3")
    os.remove(title + ".jpg")
