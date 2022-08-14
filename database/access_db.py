from config import *
from database.database import Database
import pymongo

DATABASE_URL=MONGO_URL
db = Database(DATABASE_URL, "aprt_bot")
