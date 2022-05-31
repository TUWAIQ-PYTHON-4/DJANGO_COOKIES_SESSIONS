from django.db import models
#from django.utils.timezone import now

# Create your models here.

class Book(models.Model):

    title = models.CharField(max_length=512)
    desc = models.TextField()

    # To represent the model as a string
    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=124)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
