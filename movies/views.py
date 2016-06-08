from django.shortcuts import render
from .models import Movie
import sqlite3
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    data_objs = Movie.objects.all().order_by('-tomatometer')
    paginator = Paginator(data_objs, 20)
    page = request.GET.get('page')
    # print page
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data = paginator.page(paginator.num_pages)
    # print data
    return render(request,'movies/index.html',{'data':data,'current':'home'})

def bookmarked(request):
    data_objs = Movie.objects.filter(bookmarked = True).order_by('-tomatometer')
    paginator = Paginator(data_objs, 20)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data = paginator.page(paginator.num_pages)
    return render(request, 'movies/index.html',{'data':data,'current':'bookmarked'})

def seen_movies(request):
    data_objs = Movie.objects.filter(seen_status = True).order_by('-tomatometer')
    paginator = Paginator(data_objs, 20)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data = paginator.page(paginator.num_pages)
    return render(request, 'movies/index.html',{'data':data,'current':'seen'})

def unseen_movies(request):
    data_objs = Movie.objects.filter(seen_status = False).order_by('-tomatometer')
    paginator = Paginator(data_objs, 20)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        data = paginator.page(paginator.num_pages)
    return render(request, 'movies/index.html',{'data':data,'current':'unseen'})

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

def change_info(request):
    id1 = request.POST['id']
    title = request.POST['title']
    director = request.POST['director']
    year = request.POST['year']
    tomato = request.POST['tomato']
    # print id1,title,director,year,tomato
    m = Movie.objects.get(pk=int(id1))
    m.title = title
    m.director = director
    m.year = int(year)
    m.tomatometer = int(tomato)
    m.save()
    return HttpResponse('Done')
