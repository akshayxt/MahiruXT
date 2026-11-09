__help__ = """
       ONLY OF DEV USERS

This script implements a Telegram bot using the pyrogram library. 

The bot allows users with administrative privileges to manage a list 

of groups stored in a MongoDB database and perform various actions such

as adding, removing groups, and sending messages to all groups.

Commands:


- `/dgroups` : Display all group IDs stored in the database.
- `/addgroup` <group_id>: Add a group ID to the database.
- `/rmgroup` <group_id>: Remove a group ID from the database.
- `/dsave` <message>: Send a message to all groups stored in the database. If the command is replied to a message, it forwards that message to all groups.

Note:
- SUDOERS: Users with administrative privileges are allowed to execute these commands.
- MongoDB URI should be specified in the 'rax.py' file.
"""

__mod_name__ = "DATA CAVE"
