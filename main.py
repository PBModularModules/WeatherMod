import requests
import os

from base.module import command, BaseModule
from pyrogram.types import Message

class WeatherMod(BaseModule):
    @command("weather")
    async def wt_cmd(self, _, message: Message):
        weatherl = self.S["succes"]["last"]
        nocity = self.S["err"]["no_city"]
        unknownerr =self.S["err"]["unknown"]


        try:
            args = message.text.split()
            if len(args) < 2:
                await message.reply(nocity)
                return
            city = args[1]
            url = f"https://wttr.in/{city}?format=%C,%t"
            response = requests.get(url)
            weather = response.text.strip()
            await message.reply(f"{weather}")


    
        except Exception as e:
            await message.reply(f"{unknownerr} <b>{str(e)}</b>")       

            