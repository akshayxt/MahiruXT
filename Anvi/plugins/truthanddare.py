from pyrogram import Client, filters
import requests
import random
from Anvi import app

# Truth or Dare API URLs
truth_api_url = "https://api.truthordarebot.xyz/v1/truth"
dare_api_url = "https://api.truthordarebot.xyz/v1/dare"


@app.on_message(filters.command("truth"))
def get_truth(client, message):
    try:
        # Make a GET request to the Truth API
        response = requests.get(truth_api_url)
        if response.status_code == 200:
            truth_question = response.json()["question"]
            message.reply_text(f"Truth question:\n\n{truth_question}")
        else:
            message.reply_text("Failed to fetch a truth question. Please try again later.")
    except Exception as e:
        message.reply_text("An error occurred while fetching a truth question. Please try again later.")

@app.on_message(filters.command("dare"))
def get_dare(client, message):
    try:
        # Make a GET request to the Dare API
        response = requests.get(dare_api_url)
        if response.status_code == 200:
            dare_question = response.json()["question"]
            message.reply_text(f"Dare question:\n\n{dare_question}")
        else:
            message.reply_text("Failed to fetch a dare question. Please try again later.")
    except Exception as e:
        message.reply_text("An error occurred while fetching a dare question. Please try again later.")



__mod_name__ = " T-D GAMES "






__help__ ="""

Help: Truth or Dare Game

This bot allows you to play Truth or Dare by fetching questions from a Truth or Dare API.

Commands:

/truth - Get a truth question.
/dare - Get a dare question.
Usage:

/truth to get a truth question.

/dare to get a dare question.


Note:

If you encounter any issues while fetching questions, please try again later. 
If the problem persists, it could be due to connectivity issues or problems with the API.

For further assistance, feel free to contact the bot developer."""