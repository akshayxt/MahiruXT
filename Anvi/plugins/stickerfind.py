from pyrogram import Client, filters
from Anvi import app


@app.on_message(filters.command("st"))
def generate_sticker(client, message):
    if len(message.command) == 2:
        sticker_id = message.command[1]
        try:
            client.send_sticker(message.chat.id, sticker=sticker_id)
        except Exception as e:
            message.reply_text(f"Error: {e}")
    else:
        message.reply_text("Please provide a sticker ID after /st command.")



__mod_name__ = " STICKER FIND "

__help__ = """
Find Any Sticker Using  This Bot.

Use /st <sticker_id>: To Send The Sticker With Given Id In Current Chat.

- `/st <sticker id>`: Sends the sticker with given `<sticker id>` in the current chat.
"""