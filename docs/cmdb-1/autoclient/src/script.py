from lib.config.conf import settings
# from src.plugins import PluginsManager

from src.client import Agent,SSHSalt

def run():
    mode = settings.MODE

    if mode == 'agent':
        obj = Agent()
    else:
        obj = SSHSalt()

    obj.collect()