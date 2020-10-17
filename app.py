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
    r = requests.get("https://api.themoviedb.org/3/movie/"+genre+"?api_key=96c605a3f3793f8017e51b718cef1263")
    json_object = r.json()
    temp_k = json_object['genres'][0]["name"]
    temp_n = json_object['original_title']
    return temp_n + " " + temp_k
    # return render_template('movies.html')

if __name__ == "__main__":
    app.run(debug = True)

