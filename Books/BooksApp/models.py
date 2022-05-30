from django.db import models


# Create your models here.

class Books(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title+''+self.description


class Comments(models.Model):
    name = models.CharField(max_length=124)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
