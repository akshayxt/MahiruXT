from datetime import datetime

from pyrogram import filters
from pyrogram.errors import PeerIdInvalid
from pyrogram.types import Message, User

from Anvi import app


def ReplyCheck(message: Message):
    reply_id = None

    if message.reply_to_message:
        reply_id = message.reply_to_message.message_id

    elif not message.from_user.is_self:
        reply_id = message.message_id

    return reply_id


infotext = (
    "[{full_name}](tg://user?id={user_id})\n\n"
    " ➻ ᴜsᴇʀ ɪᴅ: `{user_id}`\n"
    " ➻ ғɪʀsᴛ ɴᴀᴍᴇ: `{first_name}`\n"
    " ➻ ʟᴀsᴛ ɴᴀᴍᴇ: `{last_name}`\n"
    " ➻ ᴜsᴇʀɴᴀᴍᴇ: `@{username}`\n"
    " ➻ ʟᴀsᴛ sᴇᴇɴ: `{last_online}`"
)


def LastOnline(user: User):
    if user.is_bot:
        return ""
    elif user.status == "recently":
        return "ʀᴇᴄᴇɴᴛʟʏ"
    elif user.status == "within_week":
        return "ᴡɪᴛʜɪɴ ᴛʜᴇ ʟᴀsᴛ ᴡᴇᴇᴋ"
    elif user.status == "within_month":
        return "ᴡɪᴛʜɪɴ ᴛʜᴇ ʟᴀsᴛ ᴍᴏɴᴛʜ"
    elif user.status == "long_time_ago":
        return "ᴀ ʟᴏɴɢ ᴛɪᴍᴇ ᴀɢᴏ :("
    elif user.status == "online":
        return "ᴄᴜʀʀᴇɴᴛʟʏ ᴏɴʟɪɴᴇ"
    elif user.status == "offline":
        return datetime.fromtimestamp(user.status.date).strftime(
            "%a, %d %b %Y, %H:%M:%S"
        )


def FullName(user: User):
    return user.first_name + " " + user.last_name if user.last_name else user.first_name


@app.on_message(filters.command("whois"))
async def whois(client, message):
    cmd = message.command
    if not message.reply_to_message and len(cmd) == 1:
        get_user = message.from_user.id
    elif len(cmd) == 1:
        get_user = message.reply_to_message.from_user.id
    elif len(cmd) > 1:
        get_user = cmd[1]
        try:
            get_user = int(cmd[1])
        except ValueError:
            pass
    try:
        user = await client.get_users(get_user)
    except PeerIdInvalid:
        await message.reply("I don't know that user.")
        return
    desc = await client.get_chat(get_user)
    desc = desc.description
    await message.reply_text(
        infotext.format(
            full_name=FullName(user),
            user_id=user.id,
            user_dc=user.dc_id,
            first_name=user.first_name,
            last_name=user.last_name if user.last_name else "",
            username=user.username if user.username else "",
            last_online=LastOnline(user),
            bio=desc if desc else "`ᴇᴍᴩᴛʏ.`",
        ),
        disable_web_page_preview=True,
    )



__help__ ="""


This script allows users to query information about a Telegram user using the /whois command. Below is a breakdown of its functionality:

The /whois command is used to query user information.
If used without replying to a message, it returns information about the user who issued the command.
If used as a reply to another message, it returns information about the user who sent that message.
It also accepts a user ID or username as an argument to query information about a specific user.
Information displayed includes:
User ID
First name
Last name (if available)
Username (if available)
Last seen status (e.g., recently, within a week, within a month, offline, etc.)
Bio/description (if available)
Here's a help query for the /whois command:

User Information Query

This feature allows users to query information about a Telegram user.

Command:

/whois: Query information about a user.
Usage:

Use /whois command to query information about a user.
You can use it without any arguments to get information about the user who issued the command.
Reply to a message with /whois to get information about the user who sent that message.
You can also specify a user ID or username as an argument to get information about a specific user.
Note:

This command provides information such as user ID, name, username, last seen status, and bio (if available).
Use the appropriate command or method to obtain the desired information.
If you encounter any issues or have any questions, feel free to contact the bot administrator for assistance.

"""

__mod_name__ = " WHOIS "