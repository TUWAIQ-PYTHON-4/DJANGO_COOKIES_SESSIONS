from django.contrib import admin
from .models import *

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('name','comment' ,'date')
    list_filter = ('book',)


admin.site.register(Book)
admin.site.register(Reviews,ReviewsAdmin)


