from django.contrib import admin
from .models import Editor, tags, Article

# Register your models here.
admin.site.register(Editor)
admin.site.register(tags)
admin.site.register(Article)
