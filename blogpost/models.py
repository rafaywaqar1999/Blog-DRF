from django.db import models
from django.conf import settings

class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    publication_date = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', related_name='blogposts')

    def __str__(self):
        return self.title
    
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
