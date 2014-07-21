from django.db import models

class Semester(models.Model):
    semester = models.CharField(max_length=140)
    year = models.IntegerField()    

class Song(models.Model):
    song = models.CharField(max_length=140)
    original_artist = models.CharField(max_length=140)
    soloist = models.CharField(max_length=140)
    arranger = models.CharField(max_length=140)
    semester = models.ForeignKey(Semester)
