from django.contrib import admin

# Register your models here.
from .models import Post


@admin.register(Post)
class Post(admin.ModelAdmin):
    list_display = ['title']
