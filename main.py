import asyncio
from discord.ext import commands
import discord
import os

from dotenv import load_dotenv
from src.core.bot   import SuggestionBot
from src.core.config_parser import BotConfigs
from src.suggestbtn import SuggestBtn

load_dotenv()
bot = SuggestionBot()
bot_configs = BotConfigs()

@bot.command()
#@commands.is_owner()
async def prepare(ctx: commands.Context):
    await ctx.message.channel.purge(limit=10)
    await ctx.send(file=discord.File(bot_configs.suggest_image()), view=SuggestBtn(bot))


async def main():
    await bot.start(os.getenv('token'))
    
    

asyncio.run(main())