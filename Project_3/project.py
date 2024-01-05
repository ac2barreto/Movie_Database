import pandas as pd
import requests
import sqlite3
from flask import Flask, jsonify, render_template
import sqlite3


filename = '../Project_3/imdb_clean.csv'  

data = pd.read_csv(filename)

df = pd.read_csv(filename)

df=df.rename(columns={"Unnamed: 0":"id"})
df=df.rename(columns={"gross(M)":"gross_rev"})

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
        gross_rev FLOAT
    );
''')

# Insert data into the table
df.to_sql('movies', conn, if_exists='replace', index=False)

# Close the connection
conn.close()

# ------ Creating second schema in Movies_DB for cleaner data --------

# Connect to the SQLite database
conn = sqlite3.connect('movies.db')
cursor = conn.cursor()

# Create a new table - Purpose, this table does not contain genre // only contains Unique entries
cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies_summary (
        title VARCHAR(50),
        director VARCHAR(50),
        release_year DATE,
        runtime INTEGER,
        rating FLOAT,
        metascore INTEGER,
        gross_rev FLOAT
    );
''')

# Insert data into the new table from the original table
cursor.execute('''
    INSERT INTO movies_summary (title, director, release_year, runtime, rating, metascore, gross_rev)
    SELECT DISTINCT title, director, release_year, runtime, rating, metascore, gross_rev
    FROM movies;
''')

# Commit the changes and close the connection
conn.commit()
conn.close()


#####################################################################
#####################################################################
#####################################################################
#####################################################################
#########                 FLASK SETUP          ######################
#####################################################################
#####################################################################
#####################################################################
#####################################################################
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# Route for top 100 movies table _____________

@app.route('/get-top-movies')
def top_movies():
    return render_template('topmovies.html')

@app.route('/api/get-top-movies')
def get_top_movies():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT title, director FROM movies_summary;")
    movies = cursor.fetchall()
    conn.close()
    return jsonify(movies)

# Route for movies by release year_______________
@app.route('/get-release-year')
def release_year():
    return render_template('years.html')

@app.route('/api/get-release-year')
def get_release_year():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT DISTINCT COUNT(title), release_year FROM movies GROUP BY release_year;")
    movies1 = cursor.fetchall()
    conn.close()
    return jsonify(movies1)


# Route for genre distribution data_______________

@app.route('/get-movie-genres')
def movie_genres():
    return render_template('genre.html')

@app.route('/api/get-movie-genres')
def get_movie_genres():
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT genre, COUNT(*) AS genre_count FROM movies GROUP BY genre ORDER BY genre_count DESC;")
    movies2 = cursor.fetchall()
    conn.close()
    return jsonify(movies2)


if __name__ == '__main__':
    app.run(debug=True, port=1234)