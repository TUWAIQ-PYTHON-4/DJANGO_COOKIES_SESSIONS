from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()

    def __str__(self) -> str:
        return self.title

class Comment(models.Model):
    name=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
    content=models.TextField()
    post=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='comments')
    
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self) -> str:
        return self.name