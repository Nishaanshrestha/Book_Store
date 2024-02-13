from django.contrib import admin
from .models import Book
from .models import Author,Address,Country
class CountryAdmin(admin.ModelAdmin):
    list_display=('name','code')

class BookAdmin(admin.ModelAdmin):
    list_display=('title','author','price')
    prepopulated_fields={'slug':('title',)}
    search_fields=('title','author')
    list_filter=('author','rating')

class AuthorAdmin (admin.ModelAdmin):
    list_display=('name','age','genre')
    search_fields=('name','age')
    list_filter=('age','genre')
class AuthorAddress(admin.ModelAdmin):
    pass


admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Address,AuthorAddress)
admin.site.register(Country,CountryAdmin)


# Register your models here.
