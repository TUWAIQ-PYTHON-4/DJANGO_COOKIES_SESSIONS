from cProfile import label
from django.db import models

# Create your models here.


class Books(models.Model):
    title = models.CharField(  max_length=512)
    desc = models.TextField()

    def __str__(self) -> str:
        return self.title




class Reviews(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    name = models.CharField(max_length=124)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


