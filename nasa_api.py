import requests
import json
api_key="your_api_key"
api_url="https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

def get_photos(sol,camera):
    parameters = {'sol':sol, 'camera':camera ,'api_key': api_key}
    response = requests.get(api_url,params=parameters)

    if response.status_code == 200:
        data = response.json()
        photos = data['photos']
        return photos
    else:
        print(f"Error: {response.status_code}")
        return []
