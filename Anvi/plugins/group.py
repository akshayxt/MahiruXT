__mod_name__ = "Group"

__help__ = """ `pin Command`

This command is used to pin a message in a group chat. It requires the user to reply to the message they wish to pin. The command checks if the chat is a group (since pinning is not applicable in private chats) and if the user has the necessary admin privileges to pin messages. If conditions are met, the message is pinned, and a confirmation message is sent along with an inline button to view the pinned message.

Usage: Reply to a message with /pin to pin it in the group.

pinned Command

The pinned command is used to fetch the currently pinned message in the chat. If there's a pinned message, it sends a message with an inline button linking to the pinned message.

Usage: Type `/pinned` in the chat to see the current pinned message.

`unpin` Command

This command unpin a message in a group chat, similar to the pin command, it requires the user to reply to the message they wish to unpin. It checks for group context and admin privileges. If the criteria are met, the specified message is unpinned, and a confirmation is sent with an inline button to view the message that was unpinned.

Usage: Reply to a message with `/unpin` to unpin it from the group.

`removephoto` Command

The removephoto command is designed to remove the current chat photo in a group. It validates if the command issuer has the admin rights to change group info. Upon successful validation, the chat photo is removed.

Usage: Type `/removephoto` in the group where you want to remove the current chat photo.

`setphoto` Command

This command sets a new photo for the chat from a replied message containing a photo or document. It checks for admin privileges specifically the right to change group info. The command requires the user to reply to a message with a photo or a document that should be set as the new chat photo.

Usage: Reply to a photo or document with `/setphoto` to set it as the new chat photo.

`settitle` Command

The settitle command changes the title of the group. It can work in two ways: either by replying to a message containing the new title as its text or by directly providing the new title as part of the command. It checks if the user has admin rights to change group information before proceeding.

Usage:

Reply to a message with `/settitle` where the message text is the new title.

Or type `/settitle [new title]` to set a new title directly."""