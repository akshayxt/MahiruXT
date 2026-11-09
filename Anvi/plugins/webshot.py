__help__ = """This script allows you to take a screenshot of a website by providing its URL. Here's how it works:

When the user sends a command /webss, /ss, or /webshot followed by a URL, the bot captures a screenshot of the website.
The take_ss function handles the command processing. It checks the length of the command and extracts the URL and optional parameter full (indicating whether to take a full-page screenshot) accordingly.
The take_screenshot function makes a request to a web screenshot API (https://webscreenshot.vercel.app/api) to capture the screenshot.
Once the screenshot is obtained, it is sent back to the user as a photo.
Here's a brief overview of the flow:

The bot sends a message indicating that it's capturing the screenshot.
It then attempts to capture the screenshot using the take_screenshot function.
If successful, it sends the screenshot back to the user as a photo.
If unsuccessful, it informs the user that the screenshot capture failed.
Please note that this script relies on an external web screenshot API and asynchronous HTTP client (aiohttp). Ensure you have proper network connectivity and permissions to access the API."""

__mod_name__ = " WEBSHOT "