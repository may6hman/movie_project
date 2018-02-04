from django.db import models

# Create your models here.
class Movie(models.Model):
    movie_name = models.CharField(max_length=200)
    movie_description = models.CharField(max_length=2000)
    director = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    poster_img = models.ImageField(upload_to = 'pic_folder/')
    def __str__(self):
        return self.movie_name
