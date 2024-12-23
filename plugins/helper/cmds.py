import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from plugins.func.users_sql import *
@Client.on_message(filters.command ('cmds'))
# Replace with your own App ID and App Hash

# Command handler to start the 
async def start(Client, message):
  user_id = str(message.from_user.id)
  regdata = fetchinfo(user_id)
  results = str(regdata)
  if results == 'None':
    await message.reply_text("𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥𝗘𝗗 𝗬𝗘𝗧 ⚠️. 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥 𝗙𝗜𝗥𝗦𝗧 𝗕𝗬 𝗨𝗦𝗜𝗡𝗚 /register 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘.", message.id)
  else:
  # Create initial inline buttons
    buttons = [
        [
            InlineKeyboardButton("AUTH 🔑", callback_data="auth_cmd"),
            InlineKeyboardButton("CHARGE 💳", callback_data="charge_cmd")
        ],
        [
          InlineKeyboardButton("TOOLS 🔧", callback_data="tools_cmd"),
          InlineKeyboardButton("HELPER ♻️", callback_data="helper_cmd")
        ],
        [
          InlineKeyboardButton("CLOSE 🚫", callback_data="close_cmd")
        ]
    ]
    
    # Create inline keyboard markup
    reply_markup = InlineKeyboardMarkup(buttons)
    
    # Send a message with the inline keyboard
    await message.reply(f"""
<b>Hello <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>!</b>

<b>GroundBot Checker Has plenty of Commands. We Have Auth Gates, Charge Gates, Tools, And Other Things.</b>

<b>Click Each of Them Below to Know Them Better.</b>""", reply_markup=reply_markup)

# Callback query handler
@Client.on_callback_query()
async def handle_callback_query(Client, callback_query):
    data = callback_query.data
    
    if data == "auth_cmd":
      
      response_text = f"""
<b>Hello <a href="tg://user?id={callback_query.from_user.id}">{callback_query.from_user.first_name}</a>!</b>

<b>GroundBot Checker Auth Gates.</b>

<b>Click on each one below to get to know them better.</b>"""
      buttons = [
        [
            InlineKeyboardButton("AUTH 🔑", callback_data="auth_cmd"),
            InlineKeyboardButton("CHARGE 💳", callback_data="charge_cmd")
        ],
        [
          InlineKeyboardButton("TOOLS 🔧", callback_data="tools_cmd"),
          InlineKeyboardButton("HELPER ♻️", callback_data="helper_cmd")
        ],
        [
          InlineKeyboardButton("BACK ▶️", callback_data="back_to_1"),
          InlineKeyboardButton("CLOSE 🚫", callback_data="close_cmd")
        ]
      ]
      
    elif data == "charge_cmd":
      
      response_text = f"""
<b>Hello <a href="tg://user?id={callback_query.from_user.id}">{callback_query.from_user.first_name}</a>!</b>

<b>GroundBot Checker Charge Gates.</b>

<b>Click on each one below to get to know them better.</b>"""
      buttons = [
        [
            InlineKeyboardButton("AUTH 🔑", callback_data="auth_cmd"),
            InlineKeyboardButton("CHARGE 💳", callback_data="charge_cmd")
        ],
        [
          InlineKeyboardButton("TOOLS 🔧", callback_data="tools_cmd"),
          InlineKeyboardButton("HELPER ♻️", callback_data="helper_cmd")
        ],
        [
          InlineKeyboardButton("BACK ▶️", callback_data="back_to_1"),
          InlineKeyboardButton("CLOSE 🚫", callback_data="close_cmd")
        ]
      ]
    elif data == "tools_cmd":
      
      response_text = f"""
<b>Hello <a href="tg://user?id={callback_query.from_user.id}">{callback_query.from_user.first_name}</a>!</b>

<b>GroundBot Checker Tool Gates.</b>

<b>Click on each one below to get to know them better.</b>"""
      buttons = [
        [
            InlineKeyboardButton("AUTH 🔑", callback_data="auth_cmd"),
            InlineKeyboardButton("CHARGE 💳", callback_data="charge_cmd")
        ],
        [
          InlineKeyboardButton("TOOLS 🔧", callback_data="tools_cmd"),
          InlineKeyboardButton("HELPER ♻️", callback_data="helper_cmd")
        ],
        [
          InlineKeyboardButton("BACK ▶️", callback_data="back_to_1"),
          InlineKeyboardButton("CLOSE 🚫", callback_data="close_cmd")
        ]
      ]
    elif data == "helper_cmd":
      
      response_text = f"""
<b>Hello <a href="tg://user?id={callback_query.from_user.id}">{callback_query.from_user.first_name}</a>!</b>

<b>GroundBot Checker Helper Gates.</b>

<b>Click on each one below to get to know them better.</b>"""
      buttons = [
        [
            InlineKeyboardButton("AUTH 🔑", callback_data="auth_cmd"),
            InlineKeyboardButton("CHARGE 💳", callback_data="charge_cmd")
        ],
        [
          InlineKeyboardButton("TOOLS 🔧", callback_data="tools_cmd"),
          InlineKeyboardButton("HELPER ♻️", callback_data="helper_cmd")
        ],
        [
          InlineKeyboardButton("BACK ▶️", callback_data="back_to_1"),
          InlineKeyboardButton("CLOSE 🚫", callback_data="close_cmd")
        ]
      ]
    elif data == "back_to_1":
      
      response_text = f"""
<b>Hello <a href="tg://user?id={callback_query.from_user.id}">{callback_query.from_user.first_name}</a>!</b>

<b>GroundBot Checker Has plenty of Commands. We Have Auth Gates, Charge Gates, Tools, And Other Things.</b>

<b>Click on each one below to get to know them better.</b>"""
      buttons = [
        [
            InlineKeyboardButton("AUTH 🔑", callback_data="auth_cmd"),
            InlineKeyboardButton("CHARGE 💳", callback_data="charge_cmd")
        ],
        [
          InlineKeyboardButton("TOOLS 🔧", callback_data="tools_cmd"),
          InlineKeyboardButton("HELPER ♻️", callback_data="helper_cmd")
        ],
        [
          InlineKeyboardButton("CLOSE 🚫", callback_data="close_cmd")
        ]
      ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await callback_query.message.edit(
          text=response_text,
          reply_markup=reply_markup
            )

# Entry point to start the bot
if __name__ == "__main__":
  Client.run()