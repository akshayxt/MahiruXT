############################################################## Import ##################################################################################################

import re
from pyrogram import Client, filters
from pyrogram.types import Message
from Anvi import app
from pyrogram.errors import FloodWait



############################################################### Edited massage File Delete M#############################################################################




BOT_ID = 6731911432
@app.on_edited_message(filters.group)
async def delete_edited_messages(client, edited_message):

    if edited_message.from_user.id != BOT_ID:
        await edited_message.delete()



############################################################ PDF File Delete #############################################################################################




def is_pdf(file_name):
    return file_name.endswith(".pdf")

async def delete_pdf_files(client, message):
    if message.document and is_pdf(message.document.file_name):

        user_mention = message.from_user.mention
        await message.reply_text(f"Hey {user_mention}, Madrchod Apni Ma na Chuda PDF FILE send Krke Ab @raxx_xt de Dm Mai Apni Mummy ko bhej")
        
        
        await message.delete()


@app.on_message(filters.group & ~filters.me)
async def delete_pdf_messages(client, message):
    await delete_pdf_files(client, message)



############################################################ Anti Link #############################################################################################



@app.on_message(filters.text & filters.group)
async def anti_link(client, message):
    if "http://" in message.text or "https://" in message.text:
        await message.delete()


############################################################ 15 < word deleter #########################################################################################








