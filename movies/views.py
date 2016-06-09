from django.shortcuts import render, redirect
from .models import Movie, Preferences
import sqlite3
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core import serializers

def index(request):
    m = Preferences.objects.get(pk=1)
    # print m.sort_by
    if m.sort_by == "imdb":
        data_objs = Movie.objects.all().order_by('-imdb_rating')
    elif m.sort_by == "year":
        data_objs = Movie.objects.all().order_by('year')
    elif m.sort_by == "-year":
        data_objs = Movie.objects.all().order_by('-year')
    else:
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
    return render(request,'movies/index.html',{'data':data,'current':'home', 'sort_by':m.sort_by})

def bookmarked(request):
    m = Preferences.objects.get(pk=1)
    if m.sort_by == "imdb":
        data_objs = Movie.objects.filter(bookmarked = True).order_by('-imdb_rating')
    elif m.sort_by == "year":
        data_objs = Movie.objects.filter(bookmarked = True).order_by('year')
    elif m.sort_by == "-year":
        data_objs = Movie.objects.filter(bookmarked = True).order_by('-year')
    else:
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
    return render(request, 'movies/index.html',{'data':data,'current':'bookmarked', 'sort_by':m.sort_by})

def seen_movies(request):
    m = Preferences.objects.get(pk=1)
    if m.sort_by == "imdb":
        data_objs = Movie.objects.filter(seen_status = True).order_by('-imdb_rating')
    elif m.sort_by == "year":
        data_objs = Movie.objects.filter(seen_status = True).order_by('year')
    elif m.sort_by == "-year":
        data_objs = Movie.objects.filter(seen_status = True).order_by('-year')
    else:
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
    return render(request, 'movies/index.html',{'data':data,'current':'seen', 'sort_by':m.sort_by})

def unseen_movies(request):
    m = Preferences.objects.get(pk=1)
    if m.sort_by == "imdb":
        data_objs = Movie.objects.filter(seen_status = False).order_by('-imdb_rating')
    elif m.sort_by == "year":
        data_objs = Movie.objects.filter(seen_status = False).order_by('year')
    elif m.sort_by == "-year":
        data_objs = Movie.objects.filter(seen_status = False).order_by('-year')
    else:
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
    return render(request, 'movies/index.html',{'data':data,'current':'unseen', 'sort_by':m.sort_by})

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
    imdb = request.POST['imdb']
    # print id1,title,director,year,tomato
    m = Movie.objects.get(pk=int(id1))
    m.title = title
    m.director = director
    m.year = int(year)
    m.tomatometer = int(tomato)
    m.imdb_rating = float(imdb)
    m.save()
    return HttpResponse('Done')

def change_sort_by(request):
    sort_by = request.GET['sort_by']
    current = request.GET['current']
    print sort_by
    p = Preferences.objects.get(pk=1)
    p.sort_by = sort_by
    p.save()
    if current == "home":
        return redirect('index')
    elif current == "bookmarked":
        return redirect('bookmarked')
    elif current == "seen":
        return redirect('seen_movies')
    else:
        return redirect('unseen_movies')

def search(request):
    query = request.GET['query']
    sort = Preferences.objects.get(pk=1)
    if sort.sort_by == 'tomato':
        m = Movie.objects.filter(title__contains=query).order_by('-tomatometer')
    elif sort.sort_by == 'imdb':
        m = Movie.objects.filter(title__contains=query).order_by('-imdb_rating')
    elif sort.sort_by == 'year':
        m = Movie.objects.filter(title__contains=query).order_by('year')
    elif sort.sort_by == '-year':
        m = Movie.objects.filter(title__contains=query).order_by('-year')

    # data = serializers.serialize('json',m)
    # return HttpResponse(data, content_type='application/json')
    return render(request,'movies/search_template.html', {'data':m})
