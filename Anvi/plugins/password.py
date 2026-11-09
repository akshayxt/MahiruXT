import random, os
from pyrogram import Client, filters, enums 
from Anvi import app
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@app.on_message(filters.command(["genpassword", "genpw"]))
async def password(bot, update):
    message = await update.reply_text(text="Pʀᴏᴄᴇꜱꜱɪɴɢ..")
    password = "ASDFGHJKLZXCVBNMQWERTYUIOPabcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+".lower()
    if len(update.command) > 1:
        qw = update.text.split(" ", 1)[1]
    else:
        ST = ["5", "7", "6", "9", "10", "12", "14", "8", "13"] 
        qw = random.choice(ST)
    limit = int(qw)
    random_value = "".join(random.sample(password, limit))
    txt = f"<b>Lɪᴍɪᴛ:</b> {str(limit)} \n<b>Pᴀꜱꜱᴡᴏʀᴅ: <code>{random_value}</code>"
    btn = InlineKeyboardMarkup([[InlineKeyboardButton('𝗔𝗗𝗗 𝗠𝗘', url='https://t.me/Anvixtrobot?startgroup=true')]])
    await message.edit_text(text=txt, reply_markup=btn, parse_mode=enums.ParseMode.HTML)




__help__ = """

Password Genretor

This Bot Can Generate Random Password With Different Lengths

Just Send /genpassword or /genpw followed by the number of characters you want in your password.\n\n

For Example:\n/genpassword 12 will generate a password with 12 characters long.
"""

__mod_name__ = " Password Genretor "