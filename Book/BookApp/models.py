from django.db import models


# Create your models here.

class AddBooks(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self):
        return self.title


class AddComment(models.Model):
    name = models.CharField(max_length=20)
    comment = models.TextField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
