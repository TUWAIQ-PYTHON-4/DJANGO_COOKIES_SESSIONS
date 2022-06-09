from django.db import models


class Books(models.Model):

    book_name = models.CharField(max_length=452)
    description = models.TextField()
    rating = models.IntegerField(choices=[[1, "1 Star"], [2, "2 Star"], [3, "3 Star"], [4, "4 Star"], [5, "5 Star"],
                                          [6, "6 Star"], [7, "7 Star"], [8, "8 Star"], [9, "9 Star"], [10,"10 Star"]])
    
    def __str__(self) -> str:
        return self.book_name



class Review(models.Model):
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    name = models.CharField(max_length=124)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name
