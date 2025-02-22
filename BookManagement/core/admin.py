from django.contrib import admin
from core.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'genre', 'published_year')
    search_fields = ('title',)
    list_filter = ('category',)


admin.site.register(Book, BookAdmin)
