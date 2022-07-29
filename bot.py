import os
from pyrogram import idle, filters
import requests
from config import *
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram import *
from pyrogram.types import *
import yt_dlp as youtube_dl
from pyrogram import filters, Client
from youtube_search import YoutubeSearch
from pyrogram import errors
from pyrogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent
from aiohttp import ClientSession
from Python_ARQ import ARQ

from youtubesearchpython import VideosSearch
import re
import json
import random
import re
import string

from pyrogram.types import Message
import os
import aiofiles
import aiohttp
from pyrogram import filters


import requests


from os import mkdir
from random import randint

from deezer import Client

from config import (
    download_songs,
    fetch_tracks,
    parse_deezer_url,
    thumb_down,
)

import config 
from config import *
from script import *
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid

logging.basicConfig(
    level=logging.WARNING, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

app = Client(
    "Epic Developers",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    in_memory=True,
    plugins=dict(root="module"),
)


if __name__ == "__main__":
    print("⌛Updating & Analyzing bot⏳")
    try:
        app.start()
    except (ApiIdInvalid, ApiIdPublishedFlood):
        raise Exception("Your API_ID/API_HASH is not valid.")
    except AccessTokenInvalid:
        raise Exception("Your BOT_TOKEN is not valid.")
    uname = app.get_me().username
    print(f"""@{uname} is Accepted
╔════╗────────╔═══╗
║╔╗╔╗║────────║╔══╝
╚╝║║╠╩═╦══╦╗╔╗║╚══╦══╦╦══╗
──║║║║═╣╔╗║╚╝║║╔══╣╔╗╠╣╔═╝
──║║║║═╣╔╗║║║║║╚══╣╚╝║║╚═╗
──╚╝╚══╩╝╚╩╩╩╝╚═══╣╔═╩╩══╝
──────────────────║║
──────────────────╚╝
Join For update @EpicBotsSl""")
    idle()
    app.stop()
    print("Bot stopped. Alvida!")



@bot.on_message(filters.command("deezer"))
async def link_handler(_, message):
    link = message.matches[0].group(0)
    try:
        items = await parse_deezer_url(link)
        item_type = items[0]
        item_id = items[1]
        m = await message.reply_text("Gathering information... Please Wait.")
        songs = await fetch_tracks(client, item_type, item_id)
        if item_type in ["playlist", "album", "track"]:
            randomdir = f"/tmp/{str(randint(1,100000000))}"
            mkdir(randomdir)
            for song in songs:
                PForCopy = await message.reply_photo(
                    song.get("cover"),
                    caption=f"🎧 Title : `{song['name']}`\n🎤 Artist : `{song['artist']}`\n💽 Album : `{song['album']}`\n💽 Song Number : `{song['playlist_num']}`",
                )
                path = await download_songs(song, randomdir)
                thumbnail = await thumb_down(
                    song.get("thumb"), song.get("name")
                )
                AForCopy = await message.reply_audio(
                    path,
                    performer=song.get("artist"),
                    title=f"{song.get('name')} - {song.get('artist')}",
                    caption=f"[{song['name']}](https://www.deezer.com/track/{song['deezer_id']}) | {song['album']} - {song['artist']}",
                    thumb=thumbnail,
                    duration=song["duration"],
                )
                if -1001620454933:
                    await PForCopy.copy(-1001620454933)
                    await AForCopy.copy(-1001620454933)
            await m.delete()
        elif item_type == "artist":
            await m.edit_text(
                "This Is An Artist Account Link. Send me Track, Playlist or Album Link :)"
            )
        else:
            await m.edit_text("Link Type Not Available for Download.")
    except Exception as e:
        await m.edit_text(f"Error: {e}", quote=True)



print (f"""
#╔════╗────────╔═══╗
#║╔╗╔╗║────────║╔══╝
#╚╝║║╠╩═╦══╦╗╔╗║╚══╦══╦╦══╗
#──║║║║═╣╔╗║╚╝║║╔══╣╔╗╠╣╔═╝
#──║║║║═╣╔╗║║║║║╚══╣╚╝║║╚═╗
#──╚╝╚══╩╝╚╩╩╩╝╚═══╣╔═╩╩══╝
#──────────────────║║
#──────────────────╚╝
Heh heh hee 🙂""")

bot.run()
