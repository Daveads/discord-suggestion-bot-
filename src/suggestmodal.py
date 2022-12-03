import discord
import asyncio

from src.core.config_parser import BotConfigs

botconfig = BotConfigs()

class SuggestModal(discord.ui.Modal, title='Feedback'):

    suggestion = discord.ui.TextInput(
        label='TYPE IN YOUR SUGGESTION',
        style=discord.TextStyle.short,
        placeholder='Type your suggestion here! try to be detailed as possible',
        required=True,
    )

    reason = discord.ui.TextInput(
        label='HOW WOULD THIS BENEFIT THE SERVER',
        style=discord.TextStyle.long,
        placeholder='Type you answer here...',
        required=True,
        max_length=300,
    )


    async def on_submit(self, interaction: discord.Interaction):

        # embed to suggestion channel
        chn = discord.utils.get(interaction.guild.channels, id=botconfig.guild_ids('suggestions'))

        embed = discord.Embed(color=discord.Color.blue())
        embed.set_author(name=f"{interaction.user}", icon_url=f"{interaction.user.avatar}")
        embed.add_field(name="**New suggestion**", value=f"Suggested by {interaction.user.mention}" ,inline=False)

        embed.add_field(name="Suggestion", value=f"{self.suggestion.value}" ,inline=False)

        embed.add_field(name="How would it benefit this server?", value=f"{self.reason.value}" ,inline=False)
        embed.set_footer(text=f"Powered by {interaction.guild.name}",icon_url=interaction.guild.icon.url)

        sendre = await chn.send(embed=embed)

        thumb_up = '👍'
        thumb_down = '👎'
        await sendre.add_reaction(thumb_up)
        await sendre.add_reaction(thumb_down)


        await interaction.response.send_message(f'Suggestion sent')
        await asyncio.sleep(20)
        await interaction.delete_original_response()
        

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)


    