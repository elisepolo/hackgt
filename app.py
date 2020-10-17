from flask import Flask, render_template, url_for, request
import requests
print("requests file:', requests.__file__")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies', methods=["POST"])
def movies():
    genre = request.form['genre']
    if genre == 'Action':
        genre = 16
    r = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=4d00790bd9a1c4473522227ce0b3361b&language=en-US&sort_by=popularity.desc&include_adult=false&include_video=false&page=1&with_genres=" + str(genre)+",18");
    json_object = r.json()
    movieName = json_object['results'][10]["title"]
    return movieName
    # return render_template('movies.html')

if __name__ == "__main__":
    app.run(debug = True)
