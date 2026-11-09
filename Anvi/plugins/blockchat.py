__help__ ="""

Chat Blacklisting Management

This feature allows bot administrators to blacklist or whitelist chats.

Commands:

/blchat or /blacklistchat: Blacklist a chat.

/whitelistchat or /unblacklistchat or /unblchat: Whitelist a chat.

/blchats or /blacklistedchats: View all blacklisted chats.

Usage:

Use /blchat or /blacklistchat followed by the chat ID to blacklist a chat.

Use /whitelistchat, /unblacklistchat, or /unblchat followed by the chat ID to whitelist a chat.
Use /blchats or /blacklistedchats to view all blacklisted chats.

Note:

These commands are available only to users specified in SUDOERS list.
Blacklisting a chat prevents the bot from functioning in that chat.
Whitelisting a chat reverses the effect of blacklisting, allowing the bot to function in that chat again.
Use the appropriate command with the chat ID to perform the desired action.
If you encounter any issues or have any questions, feel free to contact the bot administrator for assistance."""

__mod_name__ = " BL CHAT "