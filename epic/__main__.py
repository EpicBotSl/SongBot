from epic import bot
from os import sys,mkdir,path
from aiogram import executor
from misc import dp
import handler

if __name__ == "__main__":
    if not path.exists("cache"):
        mkdir("cache")
    bot().run()



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
