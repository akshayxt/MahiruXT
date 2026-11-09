from pyrogram import Client, filters
from datetime import datetime
import pytz
from Anvi import app


def get_current_time():
    tz = pytz.timezone('Asia/Kolkata')  # Setting the timezone to India (Kolkata)
    current_time = datetime.now(tz)
    return current_time.strftime("%Y-%m-%d %H:%M:%S %Z%z")

@app.on_message(filters.command(["Time"]))
def send_time(client, message):
    time = get_current_time()
    client.send_message(message.chat.id, f"Current time in India: {time}")




__help__ = """
This plugin gives you the current Indian Standard Time (IST).

`/Time` - To know the current IST time

- /Time : Shows you the current Indian Standard Time

"""

__mod_name__ = " TIME "