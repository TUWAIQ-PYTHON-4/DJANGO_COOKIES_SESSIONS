from django.contrib import admin
from .models import Books,Comments


class BooksAdmin(admin.ModelAdmin):
    list_display = ('title', 'description',)
    list_filter = ('title',)
    search_fields = ('title',)


class CommentsAdmin(admin.ModelAdmin):
    list_display = ('name', 'comment', 'date', 'book',)
    list_filter = ('name', 'date',)
    search_fields = ('name',)


admin.site.register(Books, BooksAdmin)
admin.site.register(Comments, CommentsAdmin)
