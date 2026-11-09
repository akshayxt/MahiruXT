

# <============================================== IMPORTS =========================================================>
from pyrogram.types import InlineKeyboardButton as ib
from telegram import InlineKeyboardButton

from Anvi import BOT_USERNAME, OWNER_ID, SUPPORT_CHAT

# <============================================== CONSTANTS =========================================================>
START_IMG = [
    "https://telegra.ph/file/f3b2776b2766e911383f0.jpg",
    "https://graph.org/file/08db66a4374af926c9bd3.jpg",
    "https://graph.org/file/7d9eaee9efe95444fb5e3.jpg",
    "https://telegra.ph/file/f71f13dc4755349c13a70.jpg",
    "https://telegra.ph/file/0b99d9768000b9fbc7a28.jpg",
    "https://telegra.ph/file/6af06601caadb0e88e8fe.jpg",
    "https://telegra.ph/file/0cd3fdfb1c37e35860167.jpg",
    "https://telegra.ph/file/0cd3fdfb1c37e35860167.jpg",
    "https://graph.org/file/a45b214adabcd86401152.jpg",
]




START_VID = PING_MP4 = [
    "https://telegra.ph/file/5ce0259747cdd75db040f.mp4",
    "https://telegra.ph/file/925d833773c3f75500255.mp4",
    "https://telegra.ph/file/3c1ca2ea64323e00426c2.mp4",
    "https://telegra.ph/file/436f9cacca9b37538dda3.mp4"

]

HEY_IMG = "https://graph.org/file/3740819ccb58317741e8e.jpg"

ALIVE_ANIMATION =  ["https://telegra.ph/file/5ce0259747cdd75db040f.mp4",
                    "https://telegra.ph/file/925d833773c3f75500255.mp4",
                    "https://telegra.ph/file/3c1ca2ea64323e00426c2.mp4",
                    "https://telegra.ph/file/436f9cacca9b37538dda3.mp4",]


FIRST_PART_TEXT = "  *ʜᴇʟʟᴏ* `{}` . . ."

PM_START_TEXT = "  *Hᴇʏ ɢᴜʏs, I ᴀᴍ Aɴᴠɪ XT , ᴀ ʜᴀᴄᴋɪɴɢ ᴛʜᴇᴍᴇ ʙᴀsᴇᴅ ʀᴏʙᴏᴛ ᴡʜɪᴄʜ ɪs ᴀ Tᴇʟᴇɢʀᴀᴍ ɢʀᴏᴜᴘ ᴍᴀɴᴀɢᴇᴍᴇɴᴛ ʙᴏᴛ ᴀɴᴅ ᴀʟsᴏ ᴀ ᴘᴏᴡᴇʀғᴜʟ ɴᴏ ʟᴀɢ ᴍᴜsɪᴄ ᴘʟᴀʏᴇʀ*"

START_BTN = [
    [
        InlineKeyboardButton(
            text=" ⛩𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝘾⛩ ",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text=" 𝙃𝙀𝙇𝙋 ", callback_data="help_back"),
    ],
    [
        InlineKeyboardButton(text=" DETAILS ", callback_data="Anvix_"),
        InlineKeyboardButton(text=" AI ", callback_data="ai_handler"),
        InlineKeyboardButton(text=" SOURCE ", callback_data="git_source"),     

    ],
    [
        InlineKeyboardButton(text=" CREATOR ", url=f"tg://user?id={OWNER_ID}"),
    ],
    
    [InlineKeyboardButton(text=" 𝘾𝙃𝘼𝙏 𝙂𝙍𝙊𝙐𝙋 ", url=f"https://t.me/Friendschat_hub"),
     InlineKeyboardButton(text=" 𝐓𝐄𝐀𝐌冬𝗫𝗧 ",url=f"https://t.me/teamx_tsupport"),
    ],
]


GROUP_START_BTN = [
    [
        InlineKeyboardButton(
            text="⇦ 𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝘾 ⇨",
            url=f"https://t.me/anvixtrobot?startgroup=true",
        ),
    ],
    [
        InlineKeyboardButton(text=" SUPPORT ", url=f"https://t.me/{SUPPORT_CHAT}"),
        InlineKeyboardButton(text=" CREATOR ", url=f"tg://user?id={OWNER_ID}"),
        
    ],
]

ALIVE_BTN = [
    [
        ib(text="UPDATES", url="https://t.me/TeamX_TSupport"),
        ib(text="SUPPORT", url="https://t.me/TeamXT_Support"),
    ],
    [
        ib(
            text="⇦ 𝘼𝘿𝘿 𝙈𝙀 𝙏𝙊 𝙔𝙊𝙐𝙍 𝙂𝘾 ⇨",
            url=f"https://t.me/Anvixtrobot?startgroup=true",
        ),
    ],
]

HELP_STRINGS = """
  *Rax-Anvix*  

☉ *Here, you will find a list of all the available commands.*

ᴀʟʟ ᴄᴏᴍᴍᴀɴᴅs ᴄᴀɴ ʙᴇ ᴜsᴇᴅ ᴡɪᴛʜ : /
"""
