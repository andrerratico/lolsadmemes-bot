import requests
import json
from riotwatcher import LolWatcher, ApiError

lol_watcher = LolWatcher("RGAPI-9f79ef11-0fe3-4deb-963a-b84708bc1d59")
region = "la1"
    
def get_sumId(name) -> bool:
    id = lol_watcher.summoner.by_name(region, name)
    return id

def get_stats(id) -> bool:
    stats = lol_watcher.league.by_summoner(region,id)
    return stats
