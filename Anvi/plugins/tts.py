from pyrogram import Client, filters
from gtts import gTTS
from Anvi import app


@app.on_message(filters.command('tts'))
def text_to_speech(client, message):
    text = message.text.split(' ', 1)[1]
    tts = gTTS(text=text, lang='hi')
    tts.save('speech.mp3')
    client.send_audio(message.chat.id, 'speech.mp3')

#                                 #
__help__ ="""

Text-to-Speech Bot (TTS)

This bot converts text messages into speech using Google Text-to-Speech (gTTS) API.

Command:

/tts [text] - Convert the given text into speech.

Usage:

Send /tts [your text] to the bot.
Replace [your text] with the text you want to convert into speech.
Example:

/tts Hello, how are you?
Note:

This bot supports text-to-speech conversion in Hindi (lang='hi'). You can modify the lang parameter in the code to support different languages.
The bot will send the speech audio file in the same chat where the command is executed.
Make sure to include a space after the command (/tts) followed by the text you want to convert.
The generated audio file will be sent as an audio message.
If you encounter any issues or have any questions, feel free to contact the bot developer for assistance."""

__mod_name__ = " TTS "
