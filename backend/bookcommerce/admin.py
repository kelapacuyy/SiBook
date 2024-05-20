from django.contrib import admin
from .models import Address, Customer, Series, Author, Genre, Book, Cart, CartItem, Order, OrderItem

admin.site.register(Address)
admin.site.register(Customer)
admin.site.register(Series)
admin.site.register(Author)
admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)