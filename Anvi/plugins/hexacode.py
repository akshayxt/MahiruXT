from pyrogram import Client, filters
from Anvi import app
from Anvi import BOT_USERNAME


def hex_to_text(hex_string):
    try:
        text = bytes.fromhex(hex_string).decode('utf-8')
        return text
    except Exception as e:
        return f"Error decoding hex: {str(e)}"


def text_to_hex(text):
    hex_representation = ' '.join(format(ord(char), 'x') for char in text)
    return hex_representation


# IAM_Rax ...........................

@app.on_message(filters.command("code"))
def convert_text(_, message):
    if len(message.command) > 1:
        input_text = " ".join(message.command[1:])

        hex_representation = text_to_hex(input_text)
        decoded_text = hex_to_text(input_text)

        response_text = f"𝗜𝗻𝗽𝘂𝘁 𝗧𝗲𝘅𝘁➪\n {input_text}\n\n𝗛𝗲𝘅 𝗥𝗲𝗽𝗿𝗲𝘀𝗲𝗻𝘁𝗮𝘁𝗶𝗼𝗻➪\n {hex_representation}\n\n𝗗𝗲𝗰𝗼𝗱𝗲𝗱 𝗧𝗲𝘅𝘁➪\n {decoded_text}\n\n\n𝗕𝗬 ➪@{BOT_USERNAME}"

        message.reply_text(response_text)
    else:
        message.reply_text("Please provide text after the /code command.")


########################## COMMAND HELP ############################################################



__help__ = """

*Hexadecimal Converter*

**Commands available**:

• `/code <text>` : Convert a given text to its hex representation and vice vers

versa. If no argument is provided, it will display this help page.

**Example**:

/code Hello World!

This will give you `48 65 6c 6c 6f 20 57 6f 72 6c 64 21` which represents the string `Hello World!`.

To get back the original text from this hex representation use the same command with the hex code as an argu

ment like so `/code 48 65 6c 6c 6f 20 57 6f 72 6c 64  21`, and you'll receive `Hello World!`


"""
__mod_name__ =  " HEXACODE LANG "
