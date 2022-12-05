import asyncio
from discord.ext import commands
import discord
import os


from typing import Literal, Optional
from discord.ext.commands import Greedy, Context

from dotenv import load_dotenv
from src.core.bot   import SuggestionBot
from src.core.config_parser import BotConfigs

from src.suggestbtn import SuggestBtn
from src.replymodal import Reply

load_dotenv()
bot = SuggestionBot()
bot_configs = BotConfigs()

@bot.command()
#@commands.is_owner()
async def prepare(ctx: commands.Context):
    await ctx.message.channel.purge(limit=5)
    await ctx.send(file=discord.File(bot_configs.suggest_image()))
    embed = discord.Embed(color=discord.Color.dark_grey())
    embed.add_field(name=f"**Have a suggestion for {ctx.guild.name} ?**", value=f"Please use as much details as possible in suggestion.\n\n  Click the button below to get started with your suggestion \n **Not all suggestion requires a reply**" ,inline=False)
    await ctx.send(embed=embed, view=SuggestBtn(bot))



@bot.tree.command()
async def suggestion(interaction: discord.Interaction):
    """reply suggestion"""
    await interaction.response.send_modal(Reply())



#https://gist.github.com/AbstractUmbra/a9c188797ae194e592efe05fa129c57f
@bot.command()
@commands.guild_only()
@commands.is_owner()
async def sync(
  ctx: Context, guilds: Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
    if not guilds:
        if spec == "~":
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "*":
            ctx.bot.tree.copy_global_to(guild=ctx.guild)
            synced = await ctx.bot.tree.sync(guild=ctx.guild)
        elif spec == "^":
            ctx.bot.tree.clear_commands(guild=ctx.guild)
            await ctx.bot.tree.sync(guild=ctx.guild)
            synced = []
        else:
            synced = await ctx.bot.tree.sync()

        await ctx.send(
            f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
        )
        return

    ret = 0
    for guild in guilds:
        try:
            await ctx.bot.tree.sync(guild=guild)
        except discord.HTTPException:
            pass


        else:
            ret += 1

    await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")





async def main():
    await bot.start(os.getenv('token'))
    
    
asyncio.run(main())