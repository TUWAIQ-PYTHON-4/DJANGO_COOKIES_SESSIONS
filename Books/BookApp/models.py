from django.db import models


class Books(models.Model):
    title = models.CharField(max_length=512)
    desc = models.TextField()

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    Books = models.ForeignKey(Books, on_delete=models.CASCADE)
    name = models.CharField(max_length=124)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
