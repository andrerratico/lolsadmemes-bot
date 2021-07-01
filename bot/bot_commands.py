import os
import discord
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
    msg = discord.Embed(title="Solo/Duo Stats", description="", color=0x5CD1E5)
    msg.add_field(name=f"Ranked Solo: {stats[0]['tier']} {stats[0]['rank']}", value=f"{stats[0]['leaguePoints']}lp", inline=False)
    await ctx.send(embed = msg)

bot.run(TOKEN)

