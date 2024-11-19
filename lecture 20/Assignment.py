import requests
import json

character_url = 'https://rickandmortyapi.com/api/character'
episodes = {}

def get_episodes(episode_urls):
    episodes = []
    for episode_url in episode_urls:
        episode_data = requests.get(episode_url).json()  
        episodes.append(episode_data['name'])  

    return episodes

while character_url:
    response_data = requests.get(character_url).json()
    
    for character in response_data['results']:
        character_name = character['name']  
        episode_urls = character['episode']
        
        episode_names = get_episodes(episode_urls)
        episodes[character_name] = episode_names

    character_url = response_data.get('info', {}).get('next')

with open('episodes.json', 'w') as json_file:
    json.dump(episodes, json_file, indent=4)