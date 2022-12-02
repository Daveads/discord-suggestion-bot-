from pprint import pprint

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib




"""
for i in data['channels_id']:
    #print(i)
    ""
"""


class BotConfigs:
    def __init__ (self):
        with open("config.toml", "rb") as f:
            self.data = tomllib.load(f)

    def suggest_image(self):
        image = "img/" + self.data['image']['sugbot_image']
        return image


    def guild_ids(self, role):

        if role == 'guild_id':
            return self.data['guild_ids']['guild_id']


        elif role == 'suggestion_box':
            return self.data['guild_ids']['suggestion_box']

        elif role == 'suggestions':
            return self.data['guild_ids']['suggestions']
