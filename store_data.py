import pandas as pd
from nasa_api import get_photos
photos = get_photos(1000,'NAVCAM')
photos_list = []
for photo in photos:
    photo_data = {
        'rover': photo['rover']['name'],'camera': photo['camera']['full_name'],'earth_date': photo['earth_date'],'image_url': photo['img_src']
    }
    photos_list.append(photo_data)
    #checking 
    print(f"Rover: {photo['rover']['name']}")
    print(f"Camera: {photo['camera']['full_name']}")
    print(f"Date taken: {photo['earth_date']}")
    print(f"Image URL: {photo['img_src']}")
    print('--------------------------------------')

df = pd.DataFrame(photos_list)
df.to_csv('mars_rover_photos.csv', index=False)
