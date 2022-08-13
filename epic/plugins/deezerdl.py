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


@bot.on_message(filters.command("deezer"))
async def deezergeter(client: Client, message: Message):
    rep = await message.edit_text("`Searching For Song On Deezer.....`")
    sgname = get_text(message)
    if not sgname:
        await rep.edit(
            "`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`"
        )
        return
    link = f"https://api.deezer.com/search?q={sgname}&limit=1"
    dato = r.get(url=link).json()
    match = dato.get("data")
    try:
        urlhp = match[0]
    except IndexError:
        await rep.edit("`Song Not Found. Try Searching Some Other Song`")
        return
    urlp = urlhp.get("link")
    thumbs = urlhp["album"]["cover_big"]
    thum_f = wget.download(thumbs)
    polu = urlhp.get("artist")
    replo = urlp[29:]
    urlp = f"https://starkapis.herokuapp.com/deezer/{replo}"
    datto = r.get(url=urlp).json()
    mus = datto.get("url")
    sname = f"{urlhp.get('title')}.mp3"
    doc = r.get(mus)
    await bot.send_chat_action(message.chat.id, "upload_audio")
    await rep.edit("`Downloading Song From Deezer!`")
    with open(sname, "wb") as f:
        f.write(doc.content)
    c_time = time.time()
    car = f"""
**Song Name :** {urlhp.get("title")}
**Duration :** {urlhp.get('duration')} Seconds
**Artist :** {polu.get("name")}
Music Downloaded And Uploaded By King Userbot"""
    await rep.edit(f"`Downloaded {sname}! Now Uploading Song...`")
    await bot.send_audio(
        message.chat.id,
        audio=open(sname, "rb"),
        duration=int(urlhp.get("duration")),
        title=str(urlhp.get("title")),
        performer=str(polu.get("name")),
        thumb=thum_f,
        caption=car)
    await bot.send_chat_action(message.chat.id, "cancel")
    await rep.delete()

print("""
❤️❤️❤️❤️❤️
🕊️🕊️🕊️🕊️🕊️
🌍🌍🌍🌍🌍""")
