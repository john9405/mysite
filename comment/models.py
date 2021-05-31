from django.db import models

# Create your models here.
from blog.models import Post


class Comment(models.Model):
    target = models.ForeignKey(Post, on_delete=models.CASCADE, db_constraint=False)
    content = models.CharField(max_length=2000)
