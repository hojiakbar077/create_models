from django.contrib import admin
from .models import Author, Category, Book, Review

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'bio')
    search_fields = ('name',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price', 'rating', 'availability', 'format', 'published_date')
    search_fields = ('title', 'author__name')
    list_filter = ('availability', 'categories')
    filter_horizontal = ('categories',)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('book', 'user', 'rating')
    search_fields = ('book__title', 'user')

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
