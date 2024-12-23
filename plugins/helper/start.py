from pyrogram import Client, filters

@Client.on_message(filters.command ('start'))
async def cmd_start(Client,message):
  try:
    user_id = str(message.from_user.id)
    chat_type = str(message.chat.type)
    chat_id = str(message.chat.id)
    #PLAN CHECK 
    
    texta = """
STARTING GROUNDBOT CHECKER ⚡ ■□□
      """
    edit = await message.reply_text(texta,message.id)
    textb = """
STARTING GROUNDBOT CHECKER ⚡ ■■□
      """
    edit = await Client.edit_message_text(message.chat.id,edit.id,textb)
    textc = """
STARTING GROUNDBOT CHECKER ⚡ ■■■
      """
    edit = await Client.edit_message_text(message.chat.id,edit.id,textc)
    textd = f"""
𝗛𝗲𝘆 <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a> 

WELCOME TO GROUNDBOT CHECKER. I AM CC CHECKER BOT WITH MANY TOOLS AND COMMANDS. I CAN DO MANY WORKS.

𝗧𝗬𝗣𝗘 /register 𝗧𝗢 𝗖𝗢𝗡𝗧𝗜𝗡𝗨𝗘 𝗨𝗦𝗜𝗡𝗚 𝗠𝗘🥰🥰

"""
    edit = await Client.edit_message_text(message.chat.id,edit.id,textd)
    await plan_expirychk(user_id)
  except Exception as e:
      print(e)
