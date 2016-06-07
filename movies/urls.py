from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add/$',views.add_data, name='add_data'),
    url(r'^change_seen_status/$', views.change_seen_status, name='change_seen_status')
]
