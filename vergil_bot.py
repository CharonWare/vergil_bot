import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

responses = {"power up": "https://tenor.com/view/sin-devil-trigger-original-colors-vergil-gif-14975976",
        "let's go": "https://comicvine1.cbsistatic.com/uploads/original/11125/111254307/7399261-vergil.gif",
        "long day": "https://i.pinimg.com/originals/c2/81/ac/c281ac0e6c8ad429dc2c9dd6f6d66668.gif",
        "flourish": "https://i.pinimg.com/originals/cf/10/14/cf101493741a0ba7b9336c8e66e979ac.gif",
        "what the hell": "https://64.media.tumblr.com/f455399e9c59381f31daada50d20f1b4/tumblr_pqw0l28XEx1qhfxqk_540.gif"}

class DiscordClient(discord.Client):
    async def on_ready(self):
        print("Login as")
        print(self.user)
        print("-----")

    async def on_message(self, message):
        if message.author != self.user:
            if message.content in responses:
                if message.content == responses.keys:
                    await message.channel.send(responses.values)

client = DiscordClient()
client.run(TOKEN)