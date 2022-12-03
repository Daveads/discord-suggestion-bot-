from pprint import pprint

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


class BotConfigs:
    def __init__ (self):
        with open("config.toml", "rb") as f:
            self.data = tomllib.load(f)

    def suggest_image(self):
        image = "img/" + self.data['image']['sugbot_image']
        return image


    def guild_ids(self, role):
        
        if role in self.data['guild_ids']:
            return self.data['guild_ids'][role]