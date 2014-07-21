from django.contrib import admin
from repertoire.models import Semester, Song

class SemesterAdmin(admin.ModelAdmin):
    pass

class SongAdmin(admin.ModelAdmin):
    pass

admin.site.register(Semester, SemesterAdmin)
admin.site.register(Song, SongAdmin)
