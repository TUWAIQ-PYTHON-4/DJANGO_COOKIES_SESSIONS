from django.db import models



class Book(models.Model):
    # fk user pk
    title = models.CharField(max_length=25)
    description = models.TextField()

    def __str__(self):
        return f'{self.title}'

class Reviews(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, help_text='name of the reviewer')
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add= True)

