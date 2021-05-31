from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=500)
    content = RichTextField(
        config_name='forum-post',

        # CKEDITOR.config.extraPlugins:
        extra_plugins=['someplugin'],

        # CKEDITOR.plugins.addExternal(...)
        external_plugin_resources=[(
            'someplugin',
            '/static/.../path-to-someplugin/',
            'plugin.js',
        )],
    )
