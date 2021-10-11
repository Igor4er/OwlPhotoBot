import os
from pyrogram import Client, filters

client = os.getenv('CLIENT')

app = Client(client)
