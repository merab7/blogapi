from django.db import models
from django.contrib.auth.models import User



class Category(models.Model):
    title = models.CharField(max_length=100, blank=False, null=False)

    def __str__(self) -> str:
        return  f'category name--{self.title}'

class Post(models.Model):
    title = models.CharField(blank=False, null=False, max_length=200)
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_created=True)
    category = models.ManyToManyField(Category)

    def __str__(self) -> str:
        return  f'Post name--{self.title}\nauthor--{self.author}'


class Comments(models.Model):
    content = models.TextField(blank=False, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post =  models.OneToOneField(Post, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_created=True)

    def __str__(self) -> str:
        return  f'author--{self.author}'    

