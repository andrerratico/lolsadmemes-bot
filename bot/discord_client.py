import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

client = None

def init_client():
    client = commands.Bot(command_prefix="!")

    @client.event
    async def on_ready():
        print(f'{client.user} has come to judge your ELO')
    
    return client
