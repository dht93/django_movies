import requests
import sqlite3

conn = sqlite3.connect('movies.sqlite')
cur = conn.cursor()

url='http://www.omdbapi.com/'

cur.execute('SELECT name FROM movies ')
names = [el[0] for el in cur.fetchall()]
cur.close()
conn.close()

conn = sqlite3.connect('movies_with_data1.sqlite')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS movies (title TEXT, year TEXT, director TEXT, genre TEXT, poster_url TEXT, tomatometer TEXT, imdb_rating TEXT)')
conn.commit()

count = 1
for title in names:
    p = {
    't':title,
    'tomatoes':'true'
    }
    r=requests.get(url,params=p)
    data =r.json()
    year = data.get('Year',0)
    director = data.get('Director',None)
    genre = data.get('Genre',None)
    poster_url = data.get('Poster',None)
    tomatometer = data.get('tomatoMeter',0)
    imdb_rating = data.get('imdbRating',0)
    # print type(director)
    if tomatometer=='N/A':
        tomatometer=0
    if imdb_rating=='N/A':
        imdb_rating=0.0
    try:
        year = int(year)
    except Exception as e:
        print str(e)
        print title
        year = 0
    try:
        tomatometer = int(tomatometer)
    except Exception as e:
        print str(e)
        print title
        tomatometer = 0
    try:
        imdb_rating = float(imdb_rating)
    except Exception as e:
        print str(e)
        print title
        imdb_rating = 0
    # print title, director, year, genre, poster_url, tomatometer,imdb_rating
    # print ''
    cur.execute('INSERT INTO movies VALUES (?,?,?,?,?,?,?)',(title, year, director, genre, poster_url, tomatometer, imdb_rating))
conn.commit()
