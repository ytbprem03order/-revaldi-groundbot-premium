import asyncio
from pyrogram import Client, compose, filters, enums
import re
import os
from urllib.parse import urlparse
from pyrogram.enums import ParseMode
from pathlib import Path
from defs import getcards
from plugins.func.users_sql import *

plugins = dict(root="plugins")
scrape_queue = asyncio.Queue()
ADMIN_IDS = [1164314786]
DEFAULT_LIMIT = 10000
ADMIN_LIMIT = 50000

async def main():
  user = Client( 
              "Scrapper", 
               api_id   = API_ID, 
               api_hash = API_HASH
                )
  
  bot = Client(
      "MY_BOT", 
      api_id    = API_ID, 
      api_hash  = API_HASH, 
      bot_token = BOT_TOKEN, 
      plugins   = plugins 
  )
  clients = [user, bot]
  bot.set_parse_mode(enums.ParseMode.HTML)

  @bot.on_message(filters.command('adm_test'))
  async def cmd_help(client, message):
    await message.reply_text("i am working", message.id)

  print("Done Bot Active ✅")

  await compose(clients)


asyncio.run(main())
