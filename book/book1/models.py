from django.db import models


class book(models.Model):

    title = models.CharField(max_length=512)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title+''+''+self.description

class Comment(models.Model):
    book = models.ForeignKey(book, on_delete=models.CASCADE)
    name = models.CharField(max_length=124)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


class browse(models.Model):

    name = models.CharField(max_length=512)
    comment = models.TextField()
    date = models.DateField()
