import os
from pyrogram import Client, filters
from dotenv import load_dotenv


load_dotenv()
client = os.getenv('CLIENT')

app = Client(client)
