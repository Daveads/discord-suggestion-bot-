from discord.ext import commands
import discord

from src.core.config_parser import BotConfigs
from src.suggestbtn import SuggestBtn


bot_configs = BotConfigs()


class SuggestionBot(commands.Bot):
    def __init__(self):
        intents = discord.Intents.default()
        intents.message_content = True

        super().__init__(command_prefix=commands.when_mentioned_or('$'), intents=intents)

    async def setup_hook(self) -> None:
        self.add_view(SuggestBtn(self))
        


    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        c = self.get_guild(bot_configs.guild_ids('guild_id'))
        print("guild**********", c)
        print('------')