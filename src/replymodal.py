import discord
import asyncio

from src.core.config_parser import BotConfigs

botconfig = BotConfigs()

class Reply(discord.ui.Modal, title='Feedback'):

    user_id = discord.ui.TextInput(
        label='user_id',
        style=discord.TextStyle.short,
        placeholder='input user id',
        required=True,
    )

    reply = discord.ui.TextInput(
        label='reply to suggestion',
        style=discord.TextStyle.long,
        placeholder='input reply',
        required=True,
        max_length=300,
    )


    async def on_submit(self, interaction: discord.Interaction):

        # embed to suggestion channel
        chn = discord.utils.get(interaction.guild.channels, id=botconfig.guild_ids('replysug'))

        user = await interaction.guild.fetch_member(self.user_id.value)
        
        embed = discord.Embed(color=discord.Color.darker_grey())
        embed.add_field(name=f'**Replies to** {user} Suggestion', value=f"{self.reply.value}" ,inline=False)

        embed.set_footer(text=f"{interaction.guild.name}",icon_url=interaction.guild.icon.url)

        await chn.send(user.mention,embed=embed)

        await interaction.response.send_message(f'Suggestion reply sent', ephemeral=True)
        await asyncio.sleep(10)
        await interaction.delete_original_response()
        

    async def on_error(self, interaction: discord.Interaction, error: Exception) -> None:
        await interaction.response.send_message('Oops! Something went wrong.', ephemeral=True)


    