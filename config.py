from aiogram import Bot, Dispatcher
from dotenv import dotenv_values
from database import Database
from databade_dish import DatabaseDish

token = dotenv_values(".env")["MY_BOT_TOKEN"]
bot = Bot(token=token)
dp = Dispatcher()
database = Database("db.sqlite3")
databade_dish = DatabaseDish("db.sqlite3_dish")
