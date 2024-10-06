from flask import Flask, render_template, request
from nasa_api import get_photos
import requests
import pandas as pd

app = Flask(__name__)

api_key = "your_api_key"
api_url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos"

@app.route('/', methods=['GET', 'POST'])
def index():
    photos = []
    photos_list = []
    if request.method == 'POST':
        sol = request.form.get('sol')
        camera = request.form.get('camera')
        rover = request.form.get('rover')
        photos = get_photos(rover,sol, camera)
        for photo in photos:
            photo_data = {
                'rover': photo['rover']['name'],'camera': photo['camera']['full_name'],'earth_date': photo['earth_date'],'image_url': photo['img_src']
            }
            photos_list.append(photo_data)

    return render_template('gallery.html', photos=photos_list)

if __name__ == '__main__':
    app.run(debug=True)

