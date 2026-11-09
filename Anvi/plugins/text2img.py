import asyncio
from pyrogram import Client, filters
import requests
from Anvi import app

# Define a command handler
@app.on_message(filters.command(["text2img"]))
async def text_to_image(client, message):
    # Reply to the user indicating that the query is ongoing
    query_message = await message.reply_text("Please wait, your query is ongoing...")
    
    # Extract the text from the message
    text = message.text.split(" ", 1)[1]
    
    # Make a request to the DeepAI API
    r = requests.post(
        "https://api.deepai.org/api/text2img",
        data={"text": text},
        headers={"api-key": "bcbddea0-f2bd-4b4e-af1d-225b30893fcd"}
    )
    
    # Check if the request was successful
    if r.status_code == 200:
        # Parse the response JSON
        response_json = r.json()
        
        # Check if 'output_url' key exists in the response JSON
        if 'output_url' in response_json:
            # Send the image back to the user
            sent_message = await message.reply_photo(photo=response_json["output_url"])
            
            # Delete the message containing the command
            await message.delete()
            # Delete the message sent with the image after 10 seconds (adjust as needed)
            await sent_message.delete(delay=10)
        else:
            await query_message.delete()
            await message.reply_text("Sorry, unable to generate image. Please try again later.")
    else:
        await query_message.delete()
        await message.reply_text("Sorry, something went wrong. Please try again later.")

    # Delay for 3 seconds and then delete the "Please wait" message
    await asyncio.sleep(3)
    await query_message.delete()



__help__ ="""

*DEEP AI  TEXT TO IMAGE*



This plugin is used to convert any given text into an Image using Text2Image AI by DeepAI.

Command help

`/text2img` <your_text> as a reply to this bot's message and it will generate an Image with your provided text.



`/text2img` <your text> and you will get your desired Image.</s """
__mod_name__ = " TEXT 2 IMAGE "


