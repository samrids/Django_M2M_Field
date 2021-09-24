from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50, null=False,blank=False)

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=50, null=False,blank=False)    
    authors = models.ManyToManyField(to=Author)

    def __str__(self):
        return self.title
        