from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()

    # To represent the model as a string
    def __str__(self) -> str:
        return self.title


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=124)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
