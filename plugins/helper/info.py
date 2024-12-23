#IMPORT PYROGRAM MODULE
from pyrogram import Client, filters
#Reg Data Import
from plugins.func.users_sql import *
@Client.on_message(filters.command ('info'))
async def cmd_info(Client,message):
  try:
    user_id = str(message.from_user.id)
    regdata = fetchinfo(user_id)
    results = str(regdata)
    if results=='None':
      resp = "𝗬𝗢𝗨 𝗔𝗥𝗘 𝗡𝗢𝗧 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥𝗘𝗗 𝗬𝗘𝗧 ⚠️. 𝗥𝗘𝗚𝗜𝗦𝗧𝗘𝗥 𝗙𝗜𝗥𝗦𝗧 𝗕𝗬 𝗨𝗦𝗜𝗡𝗚 /register 𝗧𝗢 𝗨𝗦𝗘 𝗠𝗘."
      await message.reply_text(resp,message.id)
    else:
      
      if message.reply_to_message:
        user_id = str(message.reply_to_message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        #PLAN CHECK 
        await plan_expirychk(user_id)
        user_id = str(message.reply_to_message.from_user.id)
        username = str(message.reply_to_message.from_user.username)
        first_name = str(message.reply_to_message.from_user.first_name)
        info = fetchinfo(user_id)
        results = str(info)
        if results=="None":
          send_info = f"""
🔍 <b>Your Info on GroundBot Checker</b>⚡
━━━━━━━━━━━━━━
👤 <b>First Name</b>: {first_name}
🆔 <b>ID</b>: <code>{user_id}</code>
📛 <b>Username</b>: @{username}
🔗 <b>Profile Link</b>: <a href="tg://user?id={message.reply_to_message.from_user.id}">Profile Link</a>
🔒 <b>TG Restrictions</b>: {message.reply_to_message.from_user.is_restricted}
🚨 <b>TG Scamtag</b>: {message.reply_to_message.from_user.is_scam}
🌟 <b>TG Premium</b>: {message.reply_to_message.from_user.is_premium}
📋 <b>Status</b>: NOT REGISTERED
💳 <b>Credit</b>: 600
💼 <b>Plan</b>: N/A
📅 <b>Plan Expiry</b>: N/A
🔑 <b>Keys Redeemed</b>: N/A
🗓 <b>Registered At</b>: N/A
"""
          await message.reply_text(send_info,message.id)
        else:
          pid = str(message.reply_to_message.from_user.id)
          await plan_expirychk(pid)
          info = fetchinfo(user_id)
          results = info
          status = results[2]
          plan = results[3]
          expiry = results[4]
          credit = results[5]
          antispam = results[6]
          antispam_time = results[7]
          totalkey = results[8]
          reg_at = results[9]
          send_info = f"""
🔍 <b>Your Info on GroundBot Checker</b>⚡
━━━━━━━━━━━━━━
👤 <b>First Name</b>: {first_name}
🆔 <b>ID</b>: <code>{user_id}</code>
📛 <b>Username</b>: @{username}
🔗 <b>Profile Link</b>: <a href="tg://user?id={message.reply_to_message.from_user.id}">Profile Link</a>
🔒 <b>TG Restrictions</b>: {message.reply_to_message.from_user.is_restricted}
🚨 <b>TG Scamtag</b>: {message.reply_to_message.from_user.is_scam}
🌟 <b>TG Premium</b>: {message.reply_to_message.from_user.is_premium}
📋 <b>Status</b>: {status}
💳 <b>Credit</b>: {credit}
💼 <b>Plan</b>: {plan}
📅 <b>Plan Expiry</b>: {expiry}
🔑 <b>Keys Redeemed</b>: {totalkey}
🗓 <b>Registered At</b>: {reg_at}
"""
          await message.reply_text(send_info,message.id)
      else:
        user_id = str(message.from_user.id)
        chat_type = str(message.chat.type)
        chat_id = str(message.chat.id)
        #PLAN CHECK 
        await plan_expirychk(user_id)
        user_id = str(message.from_user.id)
        username = str(message.from_user.username)
        first_name = str(message.from_user.first_name)
        info = fetchinfo(user_id)
        results = str(info)
        if results=="None":
          send_info = f"""
🔍 <b>Your Info on GroundBot Checker</b>⚡
━━━━━━━━━━━━━━
👤 <b>First Name</b>: {first_name}
🆔 <b>ID</b>: <code>{user_id}</code>
📛 <b>Username</b>: @{username}
🔗 <b>Profile Link</b>: <a href="tg://user?id={message.from_user.id}">Profile Link</a>
🔒 <b>TG Restrictions</b>: {message.from_user.is_restricted}
🚨 <b>TG Scamtag</b>: {message.from_user.is_scam}
🌟 <b>TG Premium</b>: {message.from_user.is_premium}
📋 <b>Status</b>: NOT REGISTERED
💳 <b>Credit</b>: 600
💼 <b>Plan</b>: N/A
📅 <b>Plan Expiry</b>: N/A
🔑 <b>Keys Redeemed</b>: N/A
🗓 <b>Registered At</b>: N/A
"""
          await message.reply_text(send_info,message.id)
        else:
          pid = str(message.from_user.id)
          await plan_expirychk(pid)
          info = fetchinfo(user_id)
          results = info
          status = results[2]
          plan = results[3]
          expiry = results[4]
          credit = results[5]
          antispam = results[6]
          antispam_time = results[7]
          totalkey = results[8]
          reg_at = results[9]
          send_info = f"""
🔍 <b>Your Info on GroundBot Checker</b>⚡
━━━━━━━━━━━━━━
👤 <b>First Name</b>: {first_name}
🆔 <b>ID</b>: <code>{user_id}</code>
📛 <b>Username</b>: @{username}
🔗 <b>Profile Link</b>: <a href="tg://user?id={message.from_user.id}">Profile Link</a>
🔒 <b>TG Restrictions</b>: {message.from_user.is_restricted}
🚨 <b>TG Scamtag</b>: {message.from_user.is_scam}
🌟 <b>TG Premium</b>: {message.from_user.is_premium}
📋 <b>Status</b>: {status}
💳 <b>Credit</b>: {credit}
💼 <b>Plan</b>: {plan}
📅 <b>Plan Expiry</b>: {expiry}
🔑 <b>Keys Redeemed</b>: {totalkey}
🗓 <b>Registered At</b>: {reg_at}
  """
        await message.reply_text(send_info,message.id)
  except Exception as e:
      print(e)