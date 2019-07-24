# importing the requests library 
import requests 
  
api = 'newly_made_api_key'

# api-endpoint 
URL = "https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/Summoner_Name?api_key=" + api

r = requests.get(url = URL)

my_summoner_data = r.json()

URL = "https://na1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + my_summoner_data['id'] + "?api_key=" + api

r = requests.get(url = URL)

ranked_data = r.json()
print(ranked_data)