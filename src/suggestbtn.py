import discord
from src.suggestmodal import SuggestModal


class SuggestBtn(discord.ui.View):
    def __init__(self, bot):
        super().__init__(timeout=None)
        self.bot = bot
        
        
    @discord.ui.button(label='Make a suggestion', style=discord.ButtonStyle.grey, custom_id='mas')
    async def srtv(self, interaction: discord.Interaction, button: discord.ui.Button):
        #await interaction.response.send_message(view=SuggestModal(self.bot), ephemeral=True)
        await interaction.response.send_modal(SuggestModal())
        
    
"""
Gender
Age
"""
