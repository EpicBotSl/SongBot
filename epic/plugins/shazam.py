import os
import logging
import ffmpeg
import asyncio
import json
import requests
from ShazamAPI import Shazam

from pyrogram import filters, idle
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from epic import bot

@bot.on_message(filters.private & filters.audio)
async def shazam(_, message):
    user_id = message.from_user.id
    DL = "./{user_id}"
    m = await message.reply_text("**Shazam Processing**")
    a = await bot.download_media(message, DL)
    try:
       mp3_file_content_to_recognize = open(a, 'rb').read()
       shazam = Shazam(mp3_file_content_to_recognize)
       recognize_generator = shazam.recognizeSong()
       output = next(recognize_generator)
       cj = json.dumps(output)
    except:
       return await m.edit("**Error**")

    key = 'XBH4IgeIY2D40O6RAjn4r8vMav7xy6IN'
    text = cj
    t_title = "Shazam By JE"

    login_data = {
       'api_dev_key': key,
       'api_user_name': 'JasonYako',
       'api_user_password': 'Lel@takataka9'
        }
    data = {
       'api_option': 'paste',
       'api_dev_key':key,
       'api_paste_code':text,
       'api_paste_name':t_title,
       'api_paste_expire_date': 'N',
       'api_user_key': None,
       'api_paste_format': None,
        }

    login = requests.post("https://pastebin.com/api/api_login.php", data=login_data)

    r = requests.post("https://pastebin.com/api/api_post.php", data=data)

    txt = "**Shazam Done ✨\n\nBy ~ @TheTeleRoid**"
    await m.edit(txt, reply_markup=InlineKeyboardMarkup(
                                [[InlineKeyboardButton(
                                     "Results 📃", url=f"{r.text}")]]))
    os.remove(a)


print(f"""
SHaZam Alive
""")
