from flask import Flask, render_template, jsonify
import pandas as pd
app = Flask(__name__)
df = pd.read_csv('mars_rover_photos.csv')

@app.route('/')
def index():
    photos = df.to_dict(orient='records')
    return render_template('gallery.html', photos=photos)

if __name__ == "__main__":
    app.run(debug=True)
