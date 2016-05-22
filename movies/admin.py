from django.contrib import admin
from .models import Movie
# Register your models here.
# admin.site.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'director', 'year', 'genre', 'tomatometer','seen_status')
admin.site.register(Movie, MovieAdmin)
