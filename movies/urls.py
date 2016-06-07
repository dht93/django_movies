from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$',views.add_data, name='add_data'),
    url(r'^change_seen_status/$', views.change_seen_status, name='change_seen_status'),
    url(r'^change_book_status/$', views.change_book_status, name='change_book_status'),
    url(r'^bookmarked$', views.bookmarked, name='bookmarked'),
    url(r'^seen$', views.seen_movies, name='seen_movies'),
    url(r'^unseen$', views.unseen_movies, name='unseen_movies')
]
