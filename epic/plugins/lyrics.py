import os
from pyrogram import idle, filters
from config import *
import requests
import wget
import yt_dlp as youtube_dl
from pyrogram import filters, Client
from pyrogram.types import *
from pyrogram.types import Message
from pyrogram import *
from youtube_search import YoutubeSearch
from youtubesearchpython import SearchVideos
import asyncio
import math
from tswift import Song
import io
import re
import time

import aiofiles
import aiohttp
import wget

import os
from asyncio import get_running_loop
from functools import partial
from io import BytesIO
from urllib.parse import urlparse

import ffmpeg


import lyricsgenius
from youtubesearchpython import VideosSearch

from epic import bot



#▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅#



@bot.on_callback_query(filters.regex(pattern=r"lyrics"))
async def lyricssex(_, CallbackQuery):
    callback_data = CallbackQuery.data.strip()
    callback_request = callback_data.split(None, 1)[1]
    try:
        id, user_id = callback_request.split("|")
    except Exception as e:
        return await CallbackQuery.message.edit(
            f"Error Occured\n**Possible reason could be**:{e}"
        )
    url = f"https://www.youtube.com/watch?v={id}"
    print(url)
    try:
        results = VideosSearch(url, limit=1)
        for result in results.result()["result"]:
            title = result["title"]
    except Exception as e:
        return await CallbackQuery.answer(
            "Sound not found. Youtube issues.", show_alert=True
        )
    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    t = re.sub(r"[^\w]", " ", title)
    y.verbose = False
    S = y.search_song(t, get_full_info=False)
    if S is None:
        return await CallbackQuery.answer(
            "Lyrics not found :p", show_alert=True
        )
    await CallbackQuery.message.delete()
    userid = CallbackQuery.from_user.id
    usr = f"[{CallbackQuery.from_user.first_name}](tg://user?id={userid})"
    xxx = f"""
▇▃▇▆▇▊▋ **{S.title}** ▊▇▆▅▄▅

ʙʏ: ||{S.artist}||


__{S.lyrics}__"""
    if len(xxx) > 4096:
        filename = "lyrics.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(xxx.strip()))
        await CallbackQuery.message.reply_document(
            document=filename,
            caption=f"**OUTPUT:**\n\n`Lyrics`",
            quote=False,
        )
        os.remove(filename)
    else:
        await CallbackQuery.message.reply_text(xxx)


@bot.on_message(filters.command("lyrics"))
async def lrsearch(_, message: Message):
    if len(message.command) < 2:
        return await message.reply_text("**Usage:**\n\n/lyrics [ Music Name]")
    m = await message.reply_text("Searching Lyrics")
    query = message.text.split(None, 1)[1]
    x = "OXaVabSRKQLqwpiYOn-E4Y7k3wj-TNdL5RfDPXlnXhCErbcqVvdCF-WnMR5TBctI"
    y = lyricsgenius.Genius(x)
    y.verbose = False
    S = y.search_song(query, get_full_info=False)
    if S is None:
        return await m.edit("Lyrics not found :p")
    xxx = f"""
▇▅▃▇▆▇ **{S.title}** ▇▆▅▄▅▇

ʙʏ : ||{S.artist}||


__{S.lyrics}__"""
    if len(xxx) > 4096:
        await m.delete()
        filename = "lyrics.txt"
        with open(filename, "w+", encoding="utf8") as out_file:
            out_file.write(str(xxx.strip()))
        await message.reply_document(
            document=filename,
            caption=f"**OUTPUT:**\n\n`Lyrics`",
            quote=False,
        )
        os.remove(filename)
    else:
        await m.edit(xxx)

print("""
▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅▅
""")
