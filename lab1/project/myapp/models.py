from django.db import models

class Book(models.Model):
    title= models.CharField(max_length=215)
    desc= models.TextField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=124)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)