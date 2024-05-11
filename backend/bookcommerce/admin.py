from django.contrib import admin
from .models import Address, Customer, Series, Author, Genre, Book

admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(Series)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)