from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, View
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .models import Author, Series, Book, Cart, CartItem, Order, OrderItem, Shipment, Payment, Address
from .forms import UserRegisterForm, AddressForm, ProfilePictureForm, CustomPasswordChangeForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Akun {username} berhasil dibuat! Silakan log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'bookcommerce/register.html', {'form': form})

class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    success_url = reverse_lazy('home')

    def get_success_url(self):
        return self.success_url

class BookListView(ListView):
    model = Book
    template_name = 'bookcommerce/index.html'
    context_object_name = 'books'
    ordering = ['title']

class BookDetailView(View):
    def get(self, request, pk, *args, **kwargs):
        book = Book.objects.get(pk=pk)
        self.current_book = book

        context = {
            'book': book,
        }

        return render(request, 'bookcommerce/book_detail.html', context)

@login_required
def add_to_cart(request, book_id):
    if request.method == 'POST':
        book = get_object_or_404(Book, id=book_id)
        quantity = int(request.POST.get('quantity', 1))  # Default to 1 if not provided
        cart, created = Cart.objects.get_or_create(customer=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)
        if not created:
            cart_item.quantity += quantity
            cart_item.save()
        else:
            cart_item.quantity = quantity
            cart_item.save()
        messages.success(request, f"Berhasil menambahkan {quantity} {book.title}(s) ke dalam keranjang!")
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', reverse('home')))
    else:
        return HttpResponseRedirect(reverse('home'))  # Redirect if not a POST request

@login_required
def cart_detail(request):
    cart, created = Cart.objects.get_or_create(customer=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = sum(item.book.price * item.quantity for item in cart_items)

    return render(request, 'bookcommerce/cart_detail.html', {
        'cart': cart,
        'cart_items': cart_items,
        'total_price': total_price
    })

@login_required
@require_POST
def update_cart_item(request, item_id):
    action = request.POST.get('action')
    item = get_object_or_404(CartItem, id=item_id)
    
    if action == 'increase':
        item.quantity += 1
    elif action == 'decrease' and item.quantity > 1:
        item.quantity -= 1
    item.save()
    
    return redirect('cart_detail')

@login_required
@require_POST
def delete_cart_item(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart_detail')

@login_required
@require_POST
def delete_all_cart_items(request):
    cart = get_object_or_404(Cart, customer=request.user)
    cart.items.all().delete()
    return redirect('cart_detail')

@login_required
def checkout(request):
    book_id = None
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        if book_id:
            book = get_object_or_404(Book, id=book_id)
        else:  
            cart = get_object_or_404(Cart, customer=request.user)

    shipments = Shipment.objects.all()
    payments = Payment.objects.all()
    cart = Cart.objects.get(customer=request.user)
    book = Book.objects.get(id=book_id) if book_id else None

    return render(request, 'bookcommerce/checkout.html', {
        'shipments': shipments,
        'payments': payments,
        'cart_items': cart.items.all(),
        'total_price': sum(item.book.price * item.quantity for item in cart.items.all()),
        'book': book,
    })

@login_required
def payment(request):
    book_id = None
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        address_id = request.POST.get('address')
        shipment_id = request.POST.get('shipment')
        payment_id = request.POST.get('payment')

        if not address_id or not shipment_id or not payment_id:
            messages.error(request, "Mohon lengkapi semua informasi!")
            return redirect('checkout')

        shipment = get_object_or_404(Shipment, id=shipment_id)
        payment = get_object_or_404(Payment, id=payment_id)

        if book_id:
            book = get_object_or_404(Book, id=book_id)
            order = Order.objects.create(
                customer=request.user,
                address=request.user.address,
                shipment=shipment,
                payment=payment
            )
            OrderItem.objects.create(order=order, book=book, quantity=1)
        else:  
            cart = get_object_or_404(Cart, customer=request.user)
            order = Order.objects.create(
                customer=request.user,
                address=request.user.address,
                shipment=shipment,
                payment=payment
            )
            for item in cart.items.all():
                OrderItem.objects.create(order=order, book=item.book, quantity=item.quantity)
            cart.items.all().delete()  # Clear the cart

        messages.success(request, "Order berhasil dibuat!")
        book = Book.objects.get(id=book_id) if book_id else None
        return render(request, 'bookcommerce/payment.html', {
            'shipment': shipment,
            'payment': payment,
            'order_items': order.items.all(),
            'total_price': sum(item.book.price * item.quantity for item in order.items.all()),
            'book': book,
        })

@login_required
def profile(request):
    if request.method == 'POST' and 'profile_picture' in request.FILES:
        profile_picture_form = ProfilePictureForm(request.POST, request.FILES, instance=request.user)
        if profile_picture_form.is_valid():
            profile_picture_form.save()
            messages.success(request, 'Foto profil berhasil diubah.')
            return redirect('profile')
    else:
        profile_picture_form = ProfilePictureForm(instance=request.user)
        
    return render(request, 'bookcommerce/profile.html', {
        'profile_picture_form': profile_picture_form,
    })

@login_required
def order_history(request):
    orders = Order.objects.filter(customer=request.user).order_by('-order_date')
    
    orders_with_total = []
    for order in orders:
        total_price = sum(item.book.price * item.quantity for item in order.items.all())
        orders_with_total.append((order, total_price))
    
    return render(request, 'bookcommerce/order_history.html', {
        'orders_with_total': orders_with_total,
    })

@login_required
def create_address(request):
    next_url = request.GET.get('next', reverse('profile'))  # Default to 'profile' if 'next' is not provided
    if request.method == 'POST':
        form = AddressForm(request.POST)
        if form.is_valid():
            address = form.save(commit=False)
            address.save()
            request.user.address = address
            request.user.save()
            messages.success(request, 'Alamat berhasil ditambahkan.')
            return redirect(next_url)
    else:
        form = AddressForm()
    return render(request, 'bookcommerce/address_form.html', {'form': form, 'next': next_url})

@login_required
def update_address(request, address_id):
    next_url = request.GET.get('next', reverse('profile'))  # Default to 'profile' if 'next' is not provided
    address = get_object_or_404(Address, id=address_id)
    if request.method == 'POST':
        form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            messages.success(request, 'Alamat berhasil diubah.')
            return redirect(next_url)
    else:
        form = AddressForm(instance=address)
    return render(request, 'bookcommerce/address_form.html', {'form': form, 'next': next_url})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = CustomPasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # update the session with the new password
            messages.success(request, 'Password berhasil diubah.')
            return redirect('profile')
        else:
            messages.error(request, 'Silakan perbaiki kesalahan di bawah.')
    else:
        form = CustomPasswordChangeForm(request.user)
    return render(request, 'bookcommerce/change_password.html', {'form': form})

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        search_tag = request.POST['search_tag']
        if search_tag == 'books':
            context = { 'found_books': Book.objects.filter(title__icontains=request.POST['search']), 'search_tag': search_tag, 'search':search }
        elif search_tag == 'authors':
            context = { 'found_authors': Author.objects.filter(name__icontains=request.POST['search']), 'search_tag': search_tag, 'search': search }
        elif search_tag == 'series':
            context = { 'found_series': Series.objects.filter(name__icontains=request.POST['search']), 'search_tag': search_tag, 'search': search }        
        else:
            context = { 'search_tag': search_tag }
        return render(request, 'bookcommerce/search.html', context)
    return redirect(reverse('home'))