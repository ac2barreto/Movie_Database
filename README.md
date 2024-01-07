# Lightning McQueen Movie Database:
This project is a web application built using Flask that utilizes a SQLite database to store and retrieve movie-related data. Here's a breakdown of our project:

### Data Import and Cleaning:
The project begins by importing the necessary libraries, such as pandas and SQLite.
The IMDb movie dataset is loaded from the CSV file (imdb_clean.csv) into a Pandas DataFrame (df).
The column names of the DataFrame are modified for clarity and consistency.
### SQLite Database Creation:
The SQLite database named movies.db is created.
A table named movies is created within the database to store movie-related information, including title, director, release year, runtime, genre, rating, metascore, and gross revenue.
The DataFrame (df) is then inserted into this SQLite table.
### Secondary Schema Creation:
Another table named movies_summary is created in the same movies.db database.
This table is designed for cleaner data and does not include the duplicated 'genre' column. It only contains unique entries.
Data is inserted into this new table from the original movies table, selecting distinct values for the specified columns.
### Flask Web Application Setup:
The Flask web application is initialized.
Two routes are defined for rendering HTML templates (index.html, topmovies.html, years.html, and genre.html).
### Several API routes are defined to expose data from the SQLite database as JSON.
- /api/get-top-movies: Returns distinct movie titles and directors from the movies_summary table.
- /api/get-release-year: Returns the count of distinct movie titles and release years from the movies table.
- /api/get-movie-genres: Returns the count of movies grouped by genre from the movies table.
### Running the Application:
The application is configured to run with debug mode enabled on port 1234.
Overall, the project combines data processing, database management using SQLite, and web development using Flask to create a simple web application that provides information about top movies, movie counts by release year, and genre distribution.

# Table of Contents:
- [Introduction](#introduction)
- [Usage](#usage)
- [Acknowledgements](#acknowledgemnets)
- [Authors](#authors)

# Usage:<a name="usage"></a>
From the project_3 folder, run the python file project.py. While python file is running you can use the address http://127.0.0.1:1234/ to use the app. 

# Acknowledgments:<a name="acknowledgemnets"></a>
### Data Source: 
- IMDB Top 1000 Movies https://www.kaggle.com/datasets/arthurchongg/imdb-top-1000-movies/data
### Libraries and Framework:
- Pandas
- sqlite3
- Flask
- Highcharts: "https://code.highcharts.com/highcharts.js"
### HTML Templates:
- w3.css: https://www.w3schools.com/w3css/tryit.asp?filename=tryw3css_templates_website&stacked=h
### Code Support:
- UT Austin The Data Analytics and Visualization Bootcamp: https://git.bootcampcontent.com/University-of-Texas-at-Austin/UTA-VIRT-DATA-PT-08-2023-U-LOLC/-/tree/main
### Instructional Team Support:
- Javier Vargas
- Ariel Gamino
# Authors:<a name="authors"></a>
- ac2barreto
- alanabianca 
- Arezootvk 
- fraguti14
- juandg93
