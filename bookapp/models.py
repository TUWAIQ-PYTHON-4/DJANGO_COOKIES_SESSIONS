from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    def __str__(self):
        return self.title


class Comment(models.Model):
    title = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
