from statistics import mode
from django.db import models


class Books(models.Model):

    title = models.CharField(max_length=265)
    desc  = models.TextField()
    image = models.ImageField(upload_to="Books/images")

    def __str__(self) -> str:
        return self.title


class Comments(models.Model):

    name = models.CharField(max_length=265)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey(Books, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name



