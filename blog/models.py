from django.db import models

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title=models.CharField(max_length = 150)
    content=models.TextField()
    image=models.ImageField(upload_to = "articles/")
    created_at=models.DateTimeField(auto_now_add=True)
    