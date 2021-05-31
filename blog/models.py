from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=500)
    content = RichTextUploadingField()

    def __str__(self):
        return self.title
