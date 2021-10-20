from django.contrib import admin
from .models import Post


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['title', 'created_date', 'updated_date',]
    list_display_links = ('title',)
    list_filter = ['created_date', 'updated_date']
    search_fields = ('title', 'text')

