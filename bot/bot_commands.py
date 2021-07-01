import os
from discord_client import init_client
from discord.ext import commands 
from discord.ext.commands import Context
import riot_api_connection as riot

TOKEN = os.getenv('DISCORD_TOKEN')
bot = init_client()

@bot.command(name="stats")
async def get_stats(ctx, summoner):
    invoker = riot.get_sumId(summoner)
    id = invoker['id']
    stats = riot.get_stats(id)
    await ctx.send(stats)

bot.run(TOKEN)

