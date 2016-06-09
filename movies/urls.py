from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$',views.add_data, name='add_data'),
    url(r'^change_seen_status/$', views.change_seen_status, name='change_seen_status'),
    url(r'^change_book_status/$', views.change_book_status, name='change_book_status'),
    url(r'^bookmarked/$', views.bookmarked, name='bookmarked'),
    url(r'^seen/$', views.seen_movies, name='seen_movies'),
    url(r'^unseen/$', views.unseen_movies, name='unseen_movies'),
    url(r'^change_info/$', views.change_info, name='change_info'),
    url(r'^change_sort_by/$', views.change_sort_by, name='change_sort_by'),
    url(r'^search/$', views.search, name = 'search'),
    url(r'^change_search_by', views.change_search_by, name ='change_search_by')
]
