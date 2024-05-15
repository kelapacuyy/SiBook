from django.db import models
from django.contrib.auth.models import AbstractUser

# User-related models
class Address(models.Model):
	label = models.CharField(max_length=100)
	receiver_name = models.CharField(max_length=100)
	receiver_phone = models.CharField(max_length=15)
	province = models.CharField(max_length=50)
	city = models.CharField(max_length=50)
	district = models.CharField(max_length=50)
	ward = models.CharField(max_length=50)
	zipcode = models.CharField(max_length=10)
	full_address = models.CharField(max_length=150)

	def __str__(self):
		return self.label

class Customer(AbstractUser):
    email = models.EmailField(max_length=100, unique=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True, db_constraint=False)
    
    # related_name to avoid clashes with default User model
    groups = models.ManyToManyField('auth.Group', related_name='customers')
    user_permissions = models.ManyToManyField('auth.Permission', related_name='customers')

    def __str__(self):
        return self.username

# Book related models
class Series(models.Model):
	name = models.CharField(max_length=150)

	def __str__(self):
		return self.name

class Author(models.Model):
	name = models.CharField(max_length=150)
	nationality = models.CharField(max_length=100)
	author_img = models.ImageField(upload_to='uploads/authors/')

	def __str__(self):
		return self.name

class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
	# essential attributes
	title = models.CharField(max_length=150)
	cover_img = models.ImageField(upload_to='uploads/books/')
	description = models.TextField()
	author = models.ForeignKey(Author, on_delete=models.CASCADE, default=1)
	series = models.ForeignKey(Series, on_delete=models.CASCADE, default=1)
	stock = models.IntegerField(default=0)
	price = models.IntegerField(default=0)

	# detail attributes
	isbn = models.CharField(max_length=13, unique=True, null=True)
	category = models.CharField(max_length=100, null=True)
	genres = models.ManyToManyField(Genre)
	language = models.CharField(max_length=100, null=True)
	cover_type = models.CharField(max_length=20, null=True)
	pages = models.IntegerField(default=0)
	publisher = models.CharField(max_length=100, null=True)
	publish_date = models.DateField(null=True)
	weight = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	length = models.DecimalField(max_digits=5, decimal_places=2, default=0)
	width = models.DecimalField(max_digits=5, decimal_places=2, default=0)

	def __str__(self):
		return self.title

# Order related models
class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, through='CartItem')

    def __str__(self):
        return f"Cart {self.id} - {self.customer.username}"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.book.title}"

ORDER_STATUS_CHOICES = (
    ('Pending', 'Menunggu pembayaran'),
    ('Paid', 'Menunggu konfirmasi'),
    ('Shipping', 'Sedang dikirim'),
    ('Completed', 'Pesanan Selesai'),
)

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    books = models.ManyToManyField(Book, through='OrderItem')
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, choices=ORDER_STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"Order {self.id} - {self.customer.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.book.title}"