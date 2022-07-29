from os import mkdir
from random import randint

from deezer import Client
from pyrogram import Client, filters
from config import *
from config import LOG_GROUP
from pyrogram.errors import *

from config import (
    download_songs,
    fetch_tracks,
    parse_deezer_url,
    thumb_down,
)

app = Client


@app.on_message(filters.command("deezer"))
async def link_handler(app, message):
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
                if LOG_GROUP:
                    await PForCopy.copy(LOG_GROUP)
                    await AForCopy.copy(LOG_GROUP)
            await m.delete()
        elif item_type == "artist":
            await m.edit_text(
                "This Is An Artist Account Link. Send me Track, Playlist or Album Link :)"
            )
        else:
            await m.edit_text("Link Type Not Available for Download.")
    except Exception as e:
            await m.edit_text(f"Error: {e}", quote=True)


print("natural hehe 🍎he")
