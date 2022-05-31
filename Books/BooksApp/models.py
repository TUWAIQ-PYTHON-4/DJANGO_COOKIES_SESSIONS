from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + '' + self.description


class Comments(models.Model):
    name = models.CharField(max_length=124)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Books, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.name + '' + self.comment
