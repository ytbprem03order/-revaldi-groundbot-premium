from pyrogram import Client, filters
from plugins.func.users_sql import *
@Client.on_message(filters.command ('buy'))
async def cmd_buy(Client,message):
  try:
    user_id = str(message.from_user.id)
    chat_type = str(message.chat.type)
    chat_id = str(message.chat.id)
    #PLAN CHECK 
    resp =f"""
<b>📝 GroundBot Checker ⚡ 𝗣𝗹𝗮𝗻𝘀:</b>
━━━━━━━━━━━━━━

● <b>BRONZE PLAN - 100K Credits + Premium Access For 7 Days at $5</b>

● <b>SILVER PLAN - 200K Credits + Premium Access For 14 Days at $10</b>

● <b>GOLD PLAN - 500K Credits + Premium Access For 1 Month at $20</b>

<blockquote>🏦 Payment International Method: Paypal, USDT, BTC</blockquote>

<blockquote>🏦 Payment Indonesian Method: DANA, GOPAY, OVO, SHOPEEPAY</blockquote>

<blockquote>Plan availabel 7,14,30 Days. Fully works.</blockquote>

<b><a href="tg://user?id=1164314786">-----CLICK HERE TO BUY PLAN-----</a></b>
    """
    msg1 = await message.reply_text(resp,message.id)
    await plan_expirychk(user_id)
  except Exception as e:
      print(e)