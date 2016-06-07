from django.shortcuts import render
from .models import Movie
import sqlite3
from django.http import HttpResponse

def index(request):
    data = Movie.objects.all()[:100]
    # print data
    return render(request,'movies/index.html',{'data':data})

def bookmarked(request):
    data = Movie.objects.filter(bookmarked = True)
    return render(request, 'movies/index.html',{'data':data})

def seen_movies(request):
    data = Movie.objects.filter(seen_status = True)
    return render(request, 'movies/index.html',{'data':data})

def unseen_movies(request):
    data = Movie.objects.filter(seen_status = False)
    return render(request, 'movies/index.html',{'data':data})

def change_seen_status(request):
    id_to_change = request.POST['id']
    pk = id_to_change.split('-')[1]
    print id_to_change
    m = Movie.objects.get(pk = int(pk))
    if m.seen_status == True:
        m.seen_status = False
    else:
        m.seen_status = True
    m.save()
    # print m.title
    return HttpResponse("done")

def change_book_status(request):
    id_to_change = request.POST['id']
    pk = id_to_change.split('-')[1]
    print id_to_change
    m = Movie.objects.get(pk = int(pk))
    if m.bookmarked == True:
        m.bookmarked = False
    else:
        m.bookmarked = True
    m.save()
    # print m.title
    return HttpResponse("done")

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
