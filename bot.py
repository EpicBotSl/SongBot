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

from youtubesearchpython import VideosSearch
import re
import json

import requests
from bs4 import BeautifulSoup

bot = Client(
    "EpSong Bot",
    bot_token= BOT_TOKEN,
    api_id= API_ID,
    api_hash= API_HASH,
)

#---------------------------Song Bot Epic-------------------------------------#
#-----------Song Section Epic-------------------------------------#

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))

@bot.on_message(filters.command('song'))
def song(client, message):

    user_id = message.from_user.id 
    user_name = message.from_user.first_name 
    rpk = "["+user_name+"](tg://user?id="+str(user_id)+")"

    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply("🔎 𝐬𝐞𝐚𝐫𝐜𝐡𝐢𝐧𝐠...")
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
        
        performer = f"𝙴𝚙 𝚜𝚘𝚗𝚐 𝚋𝚘𝚝"  
        duration = results[0]["duration"]
        url_suffix = results[0]["url_suffix"]
        views = results[0]["views"]

    except Exception as e:
        m.edit(
            "✖𝐜𝐚𝐧𝐧𝐨𝐭 𝐟𝐢𝐧𝐝 𝐬𝐨𝐧𝐠✖ **𝐮𝐬𝐞 𝐚𝐧𝐨𝐭𝐡𝐞𝐫 𝐤𝐞𝐲𝐰𝐨𝐫𝐝**"
        )
        print(str(e))
        return
    m.edit("📥 𝐝𝐨𝐰𝐧𝐥𝐨𝐚𝐝𝐢𝐧𝐠")
    m.edit("▱▱▱▱▱▱")
    m.edit("▰▱▱▱▱▱")
    m.edit("▰▰▱▱▱▱")
    m.edit("▰▰▰▱▱▱")
    m.edit("▰▰▰▰▱▱")
    m.edit("▰▰▰▰▰▱")
    m.edit("▰▰▰▰▰▰")
    m.edit("▢▢▢▢▢")
    m.edit("▣▢▢▢▢")
    m.edit("▣▣▢▢▢")
    m.edit("▣▣▣▢▢")
    m.edit("▣▣▣▣▢")
    m.edit("▣▣▣▣▣")
    m.edit("▢𝐒𝐞𝐧𝐝𝐢𝐧𝐠▢")
    m.edit("▣𝐒𝐞𝐧𝐝𝐢𝐧𝐠▣")
    m.edit("▢𝐒𝐞𝐧𝐝𝐢𝐧𝐠▢")
    m.edit("▣𝐒𝐞𝐧𝐝𝐢𝐧𝐠▣")
    m.edit("▢𝐒𝐞𝐧𝐝𝐢𝐧𝐠▢")
    m.edit("▣𝐒𝐞𝐧𝐝𝐢𝐧𝐠▣")
    m.edit("▢𝐒𝐞𝐧𝐝𝐢𝐧𝐠▢")
    m.edit("▣𝐒𝐞𝐧𝐝𝐢𝐧𝐠▣")
    m.edit("▢𝐒𝐞𝐧𝐝𝐢𝐧𝐠▢")
    m.edit("▣𝐒𝐞𝐧𝐝𝐢𝐧𝐠▣")
    m.edit("▢𝐒𝐞𝐧𝐝𝐢𝐧𝐠▢")
    m.edit("▣𝐒𝐞𝐧𝐝𝐢𝐧𝐠▣")
    m.edit("▢𝐒𝐞𝐧𝐝𝐢𝐧𝐠▢")
 
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = (f"""
🏷 **𝚃𝚒𝚝𝚒𝚕𝚎:** ||[{title}]({link})||
⏳ **𝙳𝚞𝚛𝚊𝚝𝚒𝚘𝚗:** ||{duration}||
👀 **𝚅𝚒𝚎𝚠𝚜:** ||{views}|| 
👤**𝚁𝚎𝚚𝚞𝚎𝚜𝚝𝚎𝚍 𝚋𝚢**: ||{message.from_user.mention()}||
📤 **𝚄𝚙𝚕𝚘𝚊𝚍𝚎𝚍 𝚋𝚢: ||[𝑬𝒑 𝒔𝒐𝒏𝒈 𝒃𝒐𝒕](https://t.me/EpSongBot)||
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
#---------------------------Song Bot Epic-------------------------------------#
#----------Inline Section Epic-------------------------------------#

@bot.on_inline_query()
async def inline(client: Client, query: InlineQuery):
    answers = []
    search_query = query.query.lower().strip().rstrip()

    if search_query == "":
        await bot.answer_inline_query(
            query.id,
            results=answers,
            switch_pm_text="ᴛʏᴩᴇ ᴀ ʏᴏᴜᴛᴜʙᴇ ᴠɪᴅᴇᴏ ɴᴀᴍᴇ...",
            switch_pm_parameter="help",
            cache_time=0
        )
    else:
        search = VideosSearch(search_query, limit=50)

        for result in search.result()["result"]:
            answers.append(
                InlineQueryResultArticle(
                    title=result["title"],
                    description="{}, {} views.".format(
                        result["duration"],
                        result["viewCount"]["short"]
                    ),
                    input_message_content=InputTextMessageContent(
                        "https://www.youtube.com/watch?v={}".format(
                            result["id"]
                        )
                    ),
                    thumb_url=result["thumbnails"][0]["url"]
                )
            )

        try:
            await query.answer(
                results=answers,
                cache_time=0
            )
        except errors.QueryIdInvalid:
            await query.answer(
                results=answers,
                cache_time=0,
                switch_pm_text="ᴇʀʀᴏʀ : sᴇᴀʀᴄʜ ᴛɪᴍᴇᴅ ᴏᴜᴛ ",
                switch_pm_parameter="",
            )

#---------------------------Song Bot Epic-------------------------------------#
#-------------------Epic-------------------------------------#
@bot.on_message(filters.command('lyric'))
async def sng(bot, message):
        hy = await message.reply_text("`Searching 🔎`")
        song = message.text
        chat_id = message.from_user.id
        rpl = lyrics(song)
        await hy.delete()
        try:
                await hy.delete()
                await Ek.send_message(chat_id, text = rpl, reply_to_message_id = message.message_id, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("Dev 🔗 ", url = f"github.com/M-fazin")], [InlineKeyboardButton("🧑‍💻 Channel", url = "https://telegram.me/EKBOTZ_UPDATE"),InlineKeyboardButton("🗃️ Source Code", url = "https://github.com/M-fazin/Lyrics-Search-Bot")]]))
        except Exception as e:
        	await message.reply_text(f"I Can't Find A Song With `{song}`", quote = True, reply_markup = InlineKeyboardMarkup([[InlineKeyboardButton("🧑‍💻 Developer", url = f"github.com/M-fazin")], [InlineKeyboardButton("🧑‍💻 Channel", url = "https://telegram.me/EKBOTZ_UPDATE"),InlineKeyboardButton("🗃️ Source Code", url = "https://github.com/M-fazin/Lyrics-Search-Bot")]]))


def search(song):
        r = requests.get(API + song)
        find = r.json()
        return find
       
def lyrics(song):
        fin = search(song)
        text = f'**🎶 Successfully Extracted Lyrics Of {song} 🎶**\n\n\n\n'
        text += f'`{fin["lyrics"]}`'
        text += '\n\n\n**||Made With ❤️ By @EpicBotsSl||**'
        return text



print (f"""
#╔════╗────────╔═══╗
#║╔╗╔╗║────────║╔══╝
#╚╝║║╠╩═╦══╦╗╔╗║╚══╦══╦╦══╗
#──║║║║═╣╔╗║╚╝║║╔══╣╔╗╠╣╔═╝
#──║║║║═╣╔╗║║║║║╚══╣╚╝║║╚═╗
#──╚╝╚══╩╝╚╩╩╩╝╚═══╣╔═╩╩══╝
#──────────────────║║
#──────────────────╚╝""")

bot.run()
