from epic import *
from pyrogram import filters
from epic import bot
from pyrogram import *
from pyrogram.types import *
from config import *
from epic.fsub import *



import re
import uuid
import socket
import platform
import os
import random
import time
import math
import json
import string
import traceback
import psutil
import asyncio
import wget
import motor.motor_asyncio
import pymongo
import aiofiles
import datetime
from pyrogram.errors.exceptions.bad_request_400 import *
from pyrogram.errors import *
from pyrogram import Client, filters
from pyrogram.errors import *
from pyrogram.types import *
from helper.decorators import humanbytes
from config import *
from database.db import Database
from asyncio import *
import heroku3
import requests
from script import *
from database.check_user import *


#+_+_$($(_??_?_!!_!!$++$+$!+$++#+:@!_()_//_/_)_))_(_+#!@!;_+"(#!;1)_)_-#+



async def send_msg(user_id, message):
    try:
        await message.copy(chat_id=user_id)
        return 200, None
    except FloodWait as e:
        await asyncio.sleep(e.x)
        return send_msg(user_id, message)
    except InputUserDeactivated:
        return 400, f"{user_id} : deactivated\n"
    except UserIsBlocked:
        return 400, f"{user_id} : user is blocked\n"
    except PeerIdInvalid:
        return 400, f"{user_id} : user id invalid\n"
    except Exception as e:
        return 500, f"{user_id} : {traceback.format_exc()}\n"
        
#------------------------------Db End---------------------------------------------------------#       

DATABASE_URL=MONGO_URL
db = Database(DATABASE_URL, "epbot")

#lfpwkq

START_BUTTON = InlineKeyboardMarkup([[
                 InlineKeyboardButton('❤️ Chanel ❤️', url="t.me/EpicBotsSl"),
                 InlineKeyboardButton('✨ Group ✨', url="t.me/EpicChats")
                 ]])

START_MSG = f"""
🎶 Welcome To Song DownloaderBot ✓

✨You Can download Song & Get lyrics Using This Bot
~ use command /help to know more about how to use
~ use command /about to know more about

❤️ Made With By @EpicBotsSl 👑
"""


HELP = f"""
**✨How to download Song ?**
Ex :
`/search Justin Bieber lonely`
or 
`/music`
`/song`

**✨Download on yt**

Ex :
`/yt Believer`

**✨How To Find Lyrics**

Ex : 
`/lyrics justin bieber boyfriend`
"""


M_back = InlineKeyboardMarkup([[
                 InlineKeyboardButton('⏎', callback_data="mback")
                 ]])


ABOUT_TXT = f"""
👀ᴅᴇᴠᴇʟᴏᴘᴇʀ : [𝔫𝔞𝔳𝔞𝔫𝔧𝔞𝔫𝔞](https://t.me/NA_VA_N_JA_NA1)
🔥ꜱᴏᴜʀᴄᴇ ᴄᴏᴅᴇ : [GITᕼᑌᗷ](https://github.com/EpicBotSl/ImNavanjana)
🔰ᴘᴏᴡᴇʀᴅ ʙʏ : [ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ](https://t.me/EpicBotsSl)
⚡ʙᴀꜱᴇᴅ ᴏɴ : [ᴘʏʀᴏɢʀᴀᴍ](https://pyrogram.org)
🚦ᴍᴀᴅᴇ ᴡɪᴛʜ : [ᴘʏᴛʜᴏɴ](https://python.org)
      [ᴇᴘɪᴄ ᴅᴇᴠᴇʟᴏᴘᴇʀꜱ 🇱🇰](https://t.me/EpicBotsSl)
"""


@bot.on_message(filters.command("start"))
async def start(bot, message):
    if await forcesub(bot, message):
       return
    chat_id = message.from_user.id
    if not await db.is_user_exist(chat_id):
        data = await bot.get_me()
        BOT_USERNAME = data.username
        await db.add_user(chat_id)
        if -1001741009206:
            await bot.send_message(
                -1001741009206,
                f"#NEWUSER: \n\n**User:** [{message.from_user.first_name}](tg://user?id={message.from_user.id})\n\**ID:**{message.from_user.id}\n Started @{BOT_USERNAME} !!",
            )
        else:
            logging.info(f"#NewUser :- Name : {message.from_user.first_name} ID : {message.from_user.id}")
    await message.delete()
    file_id = "CAACAgUAAxkBAAIzBWL6LFyjDEKrvpH8L0AdzQABvNpLAwAC5gcAAgPB0FehQqCWEtALkR4E"
    await bot.send_sticker(message.chat.id, file_id)
    text = f"""
💞 Hello ||{message.from_user.first_name}||

**🎶 Welcome To [Ep Song Bot](t.me/Epsongbot) ✓**

✨You Can download Song & Get lyrics Using This Bot
__~ use command /help to know more about how to use
~ use command /about to know more about__


**❤️ Made With By @EpicBotsSl 👑**"""
    reply_markup = START_BUTTON  
    await message.reply_text(
        text=text,
        reply_markup=reply_markup,
        disable_web_page_preview=True,
        quote=True
    )
#=•=•=•=•=•=•=•Users Counts=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#

@bot.on_message(filters.command("stats")) 
async def startprivatsjwe(bot, message):
    countb = await db.total_users_count()
    countb = await db.total_users_count()
    count = await bot.get_chat_members_count(-1001620454933)
    counta = await bot.get_chat_members_count(-1001620454933)
    text=f"""
 ❍ Song 𝐁𝐎𝐓 𝐔𝐒𝐄𝐑𝐒 ❍ : **{countb}**
 """
    await bot.send_sticker(message.chat.id, random.choice(STAT_STICKER))
    await bot.send_message(message.chat.id, text=text)

STAT_STICKER = ["CAACAgQAAxkBAAEFHRditZFgRBAPm-9bkFJUQKOjSEgxoQACfwsAAmgpeVF2roP_0GLhzykE",
                "CAACAgQAAxkBAAEFHRVitZFYQ_EPOF7Y1GenAAHZOfu6xNIAAj4MAAKd3llQRh5-qJlCwa0pBA",
                "CAACAgQAAxkBAAEFHRNitZFVEBwdq0uFJDOvDRx2IzdoCwAC5wwAAubdSFEk6BkQ4EbQ1ikE",
                "CAACAgQAAxkBAAEFHRFitZFRwzQPYrVUQkxVP4yxF2Uw3gAC4AkAAu9GYFGTgHavjO_HLikE",
                "CAACAgQAAxkBAAEFHQ9itZFNixLf7fEZICaK8DF-Li967wACUAwAAmEq4VF8xFsUvkvQXSkE"              
         ]
#=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•Epic Bots 2022© All Rights Resived•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=•=#
#Callbacks✓


@bot.on_message(filters.command("help"))
async def shrt(client, message):
    if await forcesub(client, message):
       return
    await message.delete()
    await message.reply_photo("https://telegra.ph/file/ddaed04b00b6a96dbf7bb.jpg", caption=HELP, reply_markup=START_BUTTON)

@bot.on_message(filters.command("about"))
async def shrtrs(client, message):
    if await forcesub(client, message):
       return
    await message.delete()
    await message.reply_photo("https://telegra.ph/file/ddaed04b00b6a96dbf7bb.jpg", caption=ABOUT_TXT, reply_markup=START_BUTTON)

