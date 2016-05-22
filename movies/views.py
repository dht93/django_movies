from django.shortcuts import render
from .models import Movie
import sqlite3
from django.http import HttpResponse
# Create your views here.
def index(request):
    data = Movie.objects.all()[:20]
    # print data
    return render(request,'movies/index.html',{'data':data})
def add_data(request):
    conn = sqlite3.connect('movies_with_data1.sqlite')
    cur = conn.cursor()
    cur.execute('SELECT * FROM movies')
    data = cur.fetchall()
    for el in data[50:]:
        # print el
        try:
            m = Movie(title =el[0],year = el[1], director = el[2], genre = el[3], poster_url = el[4], tomatometer = el[5], imdb_rating = el[6], seen_status = False, bookmarked = False)
            m.save()
        except Exception as e:
            print str(e)
            # m = Movie(title =str(el[0]))
            # m.save()
            print el
    return HttpResponse('Hey')
