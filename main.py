from discord.ext import commands
import discord
from dotenv import load_dotenv
import os
from bot import Artemis

if __name__ == '__main__':
  load_dotenv()
  token = os.getenv('DISCORD_TOKEN')
  Artemis().run(token)
