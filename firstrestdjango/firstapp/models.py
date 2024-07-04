from django.db import models


class myitem(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
