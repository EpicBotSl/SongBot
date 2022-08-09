import os
from pyrogram import idle, filters
from config import *
import requests
import yt_dlp as youtube_dl
from pyrogram import filters, Client
from youtube_search import YoutubeSearch


bot = Client(
    "Epic Developers",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))

@bot.on_message(filters.command('song') & ~filters.forwarded)
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
    m.edit("⎆ ⓓⓞⓦⓝⓛⓞⓐⓓⓘⓝⓖ")
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

bot.run()
