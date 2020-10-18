from flask import Flask, render_template, url_for, request
import requests
import random 
print("requests file:', requests.__file__")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/movies', methods=["POST"])
def movies():
    genre = request.form['genre']
    genreList = []
    bool1 = True
    if request.form.get('Comedy'):
        genreList.append('35') 
    if request.form.get('Action'):
        genreList.append('28')
    if request.form.get('Drama'):
        genreList.append('18')
    if request.form.get('Animation'):
        genreList.append('16')
    if request.form.get('Family'):
        genreList.append('10751')
    if request.form.get('Thriller'):
        genreList.append('53')
    if request.form.get('History'):
        genreList.append('36')
    if request.form.get('Fantasy'):
        genreList.append('14')
    if request.form.get('Sci-Fi'):
        genreList.append('878')
    if request.form.get('Rating') == "kid":
        bool1 = False

    finalgenre = ",".join(genreList)
    r = requests.get("https://api.themoviedb.org/3/discover/movie?api_key=4d00790bd9a1c4473522227ce0b3361b&language=en-US&sort_by=popularity.desc&include_adult="+str(bool1).lower()+"&include_video=false&page=1&with_genres=" + finalgenre)
    json_object = r.json()
    indexnum = random.randint(0,len(json_object['results']))
    movieName = json_object['results'][indexnum]["title"]
    movieDesc = json_object['results'][indexnum]["overview"]
    return render_template('movies.html', pickedmovie=movieName, moviedesc=movieDesc)

if __name__ == "__main__":
    app.run(debug = True)




