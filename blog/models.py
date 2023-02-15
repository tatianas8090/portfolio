from django.db import models
import datetime

class post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to='blog/images')
    date = models.DateField(datetime.date.today)
