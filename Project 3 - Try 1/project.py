import pandas as pd
import requests
import sqlite3
from flask import Flask, jsonify, render_template
import sqlite3


filename = '../Project 3 - Try 1/imdb_clean.csv'  

data = pd.read_csv(filename)

df = pd.read_csv(filename)

df=df.rename(columns={"Unnamed: 0":"id"})

# Create a SQLite database and a table with the appropriate schema
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies (
        id INTEGER PRIMARY KEY,
        title VARCHAR(50),
        director VARCHAR(50),
        release_year INTEGER,
        runtime INTEGER,
        genre VARCHAR(20),
        rating FLOAT,
        metascore INTEGER,
        gross_m FLOAT
    );
''')

# Insert data into the table
df.to_sql('movies', conn, if_exists='replace', index=False)

# Close the connection
conn.close()


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('project.html')

@app.route('/get-movie-titles')
def get_movie_titles():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT(title) FROM movies")
    movies = cursor.fetchall()
    conn.close()
    return jsonify(movies)

@app.route('/get-movie-data/<title>')
def get_movie_data(title):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM movies WHERE title = '{title}'")
    movie_data = cursor.fetchone()
    conn.close()
    return jsonify(movie_data)

if __name__ == '__main__':
    app.run(debug=True)