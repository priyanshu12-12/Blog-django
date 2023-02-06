from django.db import models

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=20)
    author=models.CharField(max_length=20)
    blog=models.TextField()

    def __str__(self):
        return self.title
    def get_link(self):
        if self.title and '@' in self.title:
            return self.title.split('@', 1)[1]
        return None