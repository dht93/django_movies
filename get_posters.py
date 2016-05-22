import requests
import sqlite3

conn = sqlite3.connect('movies_with_data1.sqlite')
cur = conn.cursor()

cur.execute('SELECT poster_url FROM movies')
urls = [el[0] for el in cur.fetchall()]

count = 101
for url in urls[100:]:
    if not url == None:
        if len(url)>4:
            print url
            r = requests.get(url)
            f_name = str(count)+".jpg"
            f = open(f_name, 'wb')
            f.write(r.content)
            f.close()
    count += 1
