from pyrogram import Client, filters
import requests
import json
from babel import Locale

# Initialize your bot with API ID and API Hash

# Function to get flag based on country code
def get_flag(country_code):
    # Here you can implement the logic to get the flag emoji based on the country code
    return f"🇺🇸"  # This is a placeholder. You might want to create a mapping of country codes to emojis.

from plugins.func.users_sql import *
@Client.on_message(filters.command ('fake'))
async def fake_user(Client, message):
    # Extracting the country code from the command
    nat = message.text.split()[1] if len(message.command) > 1 else None
    user_id = str(message.from_user.id)
    regdata = fetchinfo(user_id)
    results = str(regdata)
    if results == 'None':
      await message.reply_text("𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥𝗘𝗗 𝗬𝗘𝗧 ⚠️. 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥 𝗙𝗜𝗥𝗦𝗧 𝗕𝗬 𝗨𝗦𝗜𝗡𝗚 /register 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘.", message.id)
    
    if not nat:
        await message.reply("❌ Please provide a valid country code! Usage: /fake <country_code>")
        return

    # Make the API request to fetch a fake user
    response = requests.get(f"https://randomuser.me/api/1.2/?nat={nat}")
    
    if response.status_code != 200:
        await message.reply("[❌] <b>Error</b> → <i>Country wasn't Found</i>!")
        return

    fake_data = response.json()
    
    if 'results' not in fake_data or not fake_data['results']:
        await message.reply("[❌] <b>Error</b> → <i>No results found!</i>")
        return
    
    fake = fake_data['results'][0]
    
    country = Locale.parse(fake['nat']).territories.get(fake['nat'])
    if not country:
        await message.reply("[❌] <b>Error</b> → <i>Enter Valid Country Code</i>!")
        return

    name = fake['name']
    loc = fake['location']
    msg = (
        f"[👤] <b>Name</b> ↯ <code>{name['title'].capitalize()}</code>. <code>{name['first'].capitalize()}</code> <code>{name['last'].capitalize()}</code>\n\n"
        f"[📧] <b>Email</b> ↯ <code>{fake['email']}</code>\n"
        f"[☎️] <b>Phone</b> ↯ <code>{fake['phone']}</code>\n\n"
        f"[🛣] <b>Street</b> ↯ <code>{loc['street']}</code>\n"
        f"[🏙] <b>City</b> ↯ <code>{loc['city'].capitalize()}</code>\n"
        f"[🗽] <b>State</b> ↯ <code>{loc['state'].capitalize()}</code>\n"
        f"[📟] <b>Postal Code</b> ↯ <code>{loc['postcode']}</code>\n"
        f"[🗺] <b>Country</b> ↯ <code>{country}</code> [<code>{get_flag(fake['nat'])}</code>]"
    )

    await message.reply(msg)

Client.run()