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

bot = Client(
    "Epic Developers",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def humanbytes(size):
    if not size:
        return ""
    power = 2 ** 10
    raised_to_pow = 0
    dict_power_n = {0: "", 1: "Ki", 2: "Mi", 3: "Gi", 4: "Ti"}
    while size > power:
        size /= power
        raised_to_pow += 1
    return str(round(size, 2)) + " " + dict_power_n[raised_to_pow] + "B"


async def progress(current, total, message, start, type_of_ps, file_name=None):
    now = time.time()
    diff = now - start
    if round(diff % 10.00) == 0 or current == total:
        percentage = current * 100 / total
        speed = current / diff
        elapsed_time = round(diff) * 1000
        if elapsed_time == 0:
            return
        time_to_completion = round((total - current) / speed) * 1000
        estimated_total_time = elapsed_time + time_to_completion
        progress_str = "{0}{1} {2}%\n".format(
            "".join("🔴" for i in range(math.floor(percentage / 10))),
            "".join("🔘" for i in range(10 - math.floor(percentage / 10))),
            round(percentage, 2),
        )

        tmp = progress_str + "{0} of {1}\nETA: {2}".format(
            humanbytes(current), humanbytes(total), time_formatter(estimated_total_time)
        )
        if file_name:
            try:
                await message.edit(
                    "{}\n**File Name:** `{}`\n{}".format(type_of_ps, file_name, tmp)
                )
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass
        else:
            try:
                await message.edit("{}\n{}".format(type_of_ps, tmp))
            except FloodWait as e:
                await asyncio.sleep(e.x)
            except MessageNotModified:
                pass

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))

def get_text(message: Message) -> [None, str]:
    text_to_return = message.text
    if message.text is None:
        return None
    if " " not in text_to_return:
        return None
    try:
        return message.text.split(None, 1)[1]
    except IndexError:
        return None

@bot.on_message(filters.command('song') & ~filters.forwarded & filters.text & filters.private)
def song(client, message):

    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply("🔎 Searching...")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        #print(results)
        title = results[0]["title"][:40]       
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f'thumb{title}.jpg'
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, 'wb').write(thumb.content)
        
        performer = f"Unknown Artist"  
        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "❌ Cannot find song use another keywords"
        )
        print(str(e))
        return
    m.edit(f"""
╭━┳━╭━╭━╮╮
┃┈┈┈┣▅╋▅┫┃
┃┈┃┈╰━╰━━━━━━╮
╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣
╲┃┈┈┈┈┈┈┈┈┈▉▉▉
╲┃┈┈┈┈┈┈┈┈┈◥▉◤
╲┃┈┈┈┈╭━┳━━━━╯
╲┣━━━━━━┫﻿
""")
    m.edit("⎆ⓓⓞⓦⓝⓛⓞⓐⓓⓘⓝⓖ")
    m.edit("⦿⦾⦾⦾")
    m.edit("⦿⦿⦾⦾")
    m.edit("⦿⦿⦿⦾")
    m.edit("⦿⦿⦿⦿")
    m.edit("⦾⦾⦾⦾")
    m.edit("⦿⦿⦿⦿")
    m.edit("⦾⦾⦾⦾")
    m.edit("⦿⦿⦿⦿")
    m.edit("⦾⦾⦾⦾")
    m.edit("⬤𝕤𝕖𝕟𝕕𝕚𝕟𝕘⬤")
    m.edit("⬤⬤𝕤𝕖𝕟𝕕𝕚𝕟𝕘⬤⬤")
    m.edit("⬤⬤⬤𝕤𝕖𝕟𝕕𝕚𝕟𝕘⬤⬤⬤")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = (f"""
💽 **𝚃𝚒𝚝𝚕𝚎 :** __[{title}]({link})__

⏳ **𝙳𝚞𝚛𝚊𝚝𝚒𝚘𝚗 :** __{duration}__

🎵 **V𝚒𝚎𝚠𝚜 :** **{views}** 

☆ **𝚁𝚎𝚚𝚞𝚎𝚜𝚝𝚎𝚍 𝚋𝚢 :** ||{message.from_user.mention()}||

👻 **𝚄𝚙𝚕𝚘𝚊𝚍𝚎𝚍 𝚋𝚢 :** ||[Ɇ₱ ₴Ø₦₲ ฿Ø₮](https://t.me/EpSongBot)||
        """)
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        s = message.reply_audio(audio_file, caption=rep, performer=performer, thumb=thumb_name, title=title, duration=dur)
        m.delete()
    except Exception as e:
        m.edit('❌ Error occurred.')
        print(e)

    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)

print(f"""
#╔════╗────────╔═══╗
#║╔╗╔╗║────────║╔══╝
#╚╝║║╠╩═╦══╦╗╔╗║╚══╦══╦╦══╗
#──║║║║═╣╔╗║╚╝║║╔══╣╔╗╠╣╔═╝
#──║║║║═╣╔╗║║║║║╚══╣╚╝║║╚═╗
#──╚╝╚══╩╝╚╩╩╩╝╚═══╣╔═╩╩══╝
#──────────────────║║
#──────────────────╚╝""")

def get_user(message: Message, text: str) -> [int, str, None]:
    asplit = None if text is None else text.split(" ", 1)
    user_s = None
    reason_ = None
    if message.reply_to_message:
        user_s = message.reply_to_message.from_user.id
        reason_ = text or None
    elif asplit is None:
        return None, None
    elif len(asplit[0]) > 0:
        user_s = int(asplit[0]) if asplit[0].isdigit() else asplit[0]
        if len(asplit) == 2:
            reason_ = asplit[1]
    return user_s, reason_


def get_readable_time(seconds: int) -> int:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        remainder, result = divmod(seconds, 60) if count < 3 else divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time


def time_formatter(milliseconds: int) -> str:
    seconds, milliseconds = divmod(int(milliseconds), 1000)
    minutes, seconds = divmod(seconds, 60)
    hours, minutes = divmod(minutes, 60)
    days, hours = divmod(hours, 24)
    tmp = (
        ((str(days) + " day(s), ") if days else "")
        + ((str(hours) + " hour(s), ") if hours else "")
        + ((str(minutes) + " minute(s), ") if minutes else "")
        + ((str(seconds) + " second(s), ") if seconds else "")
        + ((str(milliseconds) + " millisecond(s), ") if milliseconds else "")
    )
    return tmp[:-2]


def get_file_extension_from_url(url):
    url_path = urlparse(url).path
    basename = os.path.basename(url_path)
    return basename.split(".")[-1]


# Funtion To Download Song
async def download_song(url):
    song_name = f"{randint(6969, 6999)}.mp3"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                f = await aiofiles.open(song_name, mode="wb")
                await f.write(await resp.read())
                await f.close()
    return song_name


is_downloading = False


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(":"))))


#---------------------------Gen Logo Epic-------------------------------------#
#---------------------------Gen Logo Epic-------------------------------------#

@bot.on_message(filters.command("search"))
async def ytsearch(client, message):
    try:
        if len(message.command) < 2:
            await message.reply("Give me some title")
            return
        user_id = message.from_user.id
        query = " ".join(message.command[1:])
        msg = await message.reply("**Searching...**")
        results = YoutubeSearch(query, max_results=5).to_dict()
        try:
            toxxt = "**❣𝚂𝚎𝚕𝚎𝚌𝚝 𝚃𝚑𝚎 𝚜𝚘𝚗𝚐 𝚈𝚘𝚞 𝚠𝚊𝚗𝚝 𝚃𝚘 𝙳𝚘𝚠𝚗𝚕𝚘𝚊𝚍❣**\n\n"
            emojilist = ["❰❶❱", "❰❷❱", "❰❸❱", "❰❹❱", "❰❺❱"]
            for j in range(5):
                toxxt += f"{emojilist[j]} <b>ᴛɪᴛʟᴇ - [{results[j]['title']}](https://youtube.com{results[j]['url_suffix']})</b>\n"
                toxxt += f" 🕒 ╚ <b>ᴅᴜʀᴀᴛɪᴏɴ</b> - {results[j]['duration']}\n"
                toxxt += f" 👻 ╚ <b>ᴠɪᴇᴡꜱ</b> - {results[j]['views']}\n"
                toxxt += f" 📛 ╚ <b>ᴄʜᴀɴɴᴇʟ</b> - {results[j]['channel']}\n\n"

            koyboard = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "❰ ❶ ❱", callback_data=f"plll 0|{query}|{user_id}"
                        ),
                        InlineKeyboardButton(
                            "❰ ❷ ❱", callback_data=f"plll 1|{query}|{user_id}"
                        ),
                        InlineKeyboardButton(
                            "❰ ❸ ❱", callback_data=f"plll 2|{query}|{user_id}"
                        ),
                    ],
                    [
                        InlineKeyboardButton(
                            "❰ ❹ ❱", callback_data=f"plll 3|{query}|{user_id}"
                        ),
                        InlineKeyboardButton(
                            "❰ ❺ ❱", callback_data=f"plll 4|{query}|{user_id}"
                        ),
                    ],
                    [InlineKeyboardButton(text="Close", callback_data="close")],
                ]
            )
            await msg.edit(toxxt, reply_markup=koyboard, disable_web_page_preview=True)
        except Exception as e:
            await msg.edit(e)
    except Exception as e:
        await message.reply(e)


@bot.on_callback_query(filters.regex(pattern=r"plll"))
async def youtube_cb(b, cb):
    cbd = cb.data.strip()
    typed_ = cbd.split(None, 1)[1]
    try:
        x, query, useer_id = typed_.split("|")
    except:
        await cb.message.edit("Song Not Found")
        return
    useer_id = int(useer_id)
    if cb.from_user.id != useer_id:
        await cb.answer(
            "You ain't the person who requested to play the song!", show_alert=True
        )
        return
    await cb.message.edit("▱▱▱▱▱▱")
    await cb.message.edit("▰▱▱▱▱▱")
    await cb.message.edit("▰▰▱▱▱▱")
    await cb.message.edit("▰▰▰▱▱▱")
    await cb.message.edit("▰▰▰▰▱▱")
    await cb.message.edit("▰▰▰▰▰▱")
    await cb.message.edit("▰▰▰▰▰▰")

    x = int(x)
    results = YoutubeSearch(query, max_results=5).to_dict()
    resultss = results[x]["url_suffix"]
    title = results[x]["title"][:40]
    thumbnail = results[x]["thumbnails"][0]
    url = f"https://youtube.com{resultss}"
    performer = f"Unknown Artist"  
    duration = results[0]["duration"]
    url_suffix = results[0]["url_suffix"]
    views = results[0]["views"]
    channel = results[0]["channel"]
    link = f"https://youtube.com{results[0]['url_suffix']}"
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        preview = wget.download(thumbnail)
    except BaseException:
        pass
    with YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        audio_file = ydl.prepare_filename(info_dict)
        ydl.process_info(info_dict)
    await cb.message.edit("🅂🄴🄽🄳🄸🄽🄶")
    await cb.message.reply_audio(
        audio_file,
        thumb=preview,
        duration=int(info_dict["duration"]),
        caption=(f"""
 ━━━━━━━━━━━━━━━━━━━━━━━━━━┑
💽 𝙽𝚊𝚖𝚎 : __[{title}]({link})__

♪ 𝙰𝚛𝚝𝚒𝚜𝚝 : **{channel}**

⏳ 𝙳𝚞𝚛𝚊𝚝𝚒𝚘𝚗 : {duration}

💠 V𝚒𝚎𝚠𝚜 : --{views}--

┕━━━━━━━━━━━━━━━━━━━━━━━━━━━""")
    )
    try:
        os.remove(audio_file)
        os.remove(preview)
        await cb.message.delete()
    except BaseException:
        pass


@bot.on_callback_query(filters.regex(pattern=r"close"))
async def close(b, cb):
    await cb.answer("Closed!")
    await cb.message.delete()

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
▇▅▃▇▆▇▊▋__{query}__ ▊▇▆▅▄▅▇

⬬ ʙʏ : {S.artist}


{S.lyrics}"""
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
▇▅▃▇▆▇▊▋__{query}__ ▊▇▆▅▄▅▇

⬬ ʙʏ : {S.artist}


{S.lyrics}"""
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

bot.run()
