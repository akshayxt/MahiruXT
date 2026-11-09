from pyrogram import Client, filters
from pyrogram.types import Message
from Anvi import app

@app.on_message(filters.command("groupinfo", prefixes="/"))
async def get_group_status(_, message: Message):
    if len(message.command) != 2:
        await message.reply("Please provide a group username. Example: `/groupinfo YourGroupUsername`")
        return
    
    group_username = message.command[1]
    
    try:
        group = await app.get_chat(group_username)
    except Exception as e:
        await message.reply(f"Error: {e}")
        return
    
    total_members = await app.get_chat_members_count(group.id)
    group_description = group.description
    premium_acc = banned = deleted_acc = bot = 0  # You should replace these variables with actual counts.

    response_text = (
        f"➖➖➖➖➖➖➖\n"
        f"➲ GROUP NAME : {group.title} ✅\n"
        f"➲ GROUP ID : {group.id}\n"
        f"➲ TOTAL MEMBERS : {total_members}\n"
        f"➲ DESCRIPTION : {group_description or 'N/A'}\n"
        f"➲ USERNAME : @{group_username}\n"
       
        f"➖➖➖➖➖➖➖"
    )
    
    await message.reply(response_text)






# Command handler to get group status
@app.on_message(filters.command("status") & filters.group)
def group_status(client, message):
    chat = message.chat  # Chat where the command was sent
    status_text = f"Group ID: {chat.id}\n" \
                  f"Title: {chat.title}\n" \
                  f"Type: {chat.type}\n"
                  
    if chat.username:  # Not all groups have a username
        status_text += f"Username: @{chat.username}"
    else:
        status_text += "Username: None"

    message.reply_text(status_text)



__help__  ="""

*Group Info :*

- Get information about a public group by its username.

`/groupinfo <YourGroupUsername>`

Example:-

/groupinfo teamxt_support




- Get basic information of the current group.


`/status` 

Example:-

/status :  

➖➖➖➖➖➖➖
➲ GROUP NAME : 𝐓𝐄𝐀𝐌冬𝗫𝗧 ✅
➲ GROUP ID : -1001997761568
➲ TOTAL MEMBERS : 32
➲ DESCRIPTION : N/A
➲ USERNAME : @teamXt_support
➖➖➖➖➖➖➖



- You can find the `Group ID` in the link of any channel or group. It

- To find out the `GroupID`, use `/id [Optional: Message]` in that
• 

"""
__mod_name__ = " GROUP INFO "



####