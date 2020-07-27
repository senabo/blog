from django.contrib import admin
from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date')
    list_filter = ('author', 'created_date', 'published_date')


admin.site.register(Post, PostAdmin)
