from config import *
from database.database import Database

db = Database(mongodb+srv://epic:epic@cluster0.257eaxu.mongodb.net/?retryWrites=true&w=majority, "spot_dl")
