from config import *
from database.database import Database
import pymongo

DATABASE_URL=MONGO_URI
db = Database(DATABASE_URL, "aprt_bot")
