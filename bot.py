from os import path
from configparser import ConfigParser 
from shazamio import Shazam, exceptions, FactoryArtist, FactoryTrack
fimport config 
from config import *
import logging
from pyrogram import Client, idle
from pyromod import listen  # type: ignore
from pyrogram.errors import ApiIdInvalid, ApiIdPublishedFlood, AccessTokenInvalid
import logging


logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(message)s",
    handlers = [logging.FileHandler('bot.log'), logging.StreamHandler()]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)
LOGGER = logging.getLogger(__name__)



AUTH_CHATS = "-1001741009206"

class bot(Client):
    def  __init__(self):
        name = self.__class__.__name__.lower()
        super().__init__(
            ":memory:",
            plugins=dict(root=f"{name}/plugins"),
            workdir="./cache/",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            sleep_threshold=30
        )
    async def start(self):
        global BOT_INFO
        await super().start()
        BOT_INFO = await self.get_me()
        if not path.exists('/tmp/thumbnails/'):
            mkdir('/tmp/thumbnails/')
        for chat in AUTH_CHATS:
            await self.send_photo(chat,"https://telegra.ph/file/97bc8a091ac1b119b72e4.jpg","**Spotify Downloa Started**")
        LOGGER.info(f"Bot Started As {BOT_INFO.username}\n")
    
    async def stop(self,*args):
        await super().stop()
        LOGGER.info("Bot Stopped, Bye.")
#---------------------------Gen Logo Epic-------------------------------------#

    async def start(self):
        await super().start()
        print("bot started. Hi.")

    async def stop(self, *args):
        await super().stop()
        print("bot stopped. Bye.")

    async def recognize(self, path):
        return await shazam.recognize_song(path)

    async def related(self, track_id):
        try:
            return (await shazam.related_tracks(track_id=track_id, limit=50, start_from=2))['tracks']
        except exceptions.FailedDecodeJson:
            return None
    
    async def get_artist(self, query: str):
        artists = await shazam.search_artist(query=query, limit=50)
        hits = []
        try:
            for artist in artists['artists']['hits']:
                hits.append(FactoryArtist(artist).serializer())
            return hits
        except KeyError:
            return None
        
    async def get_artist_tracks(self, artist_id: int):
        tracks = []
        tem = (await shazam.artist_top_tracks(artist_id=artist_id, limit=50))['tracks']
        try:
            for track in tem:
                tracks.append(FactoryTrack(data=track).serializer())
            return tracks
        except KeyError:
            return None
