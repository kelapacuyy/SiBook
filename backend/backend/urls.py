from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from bookcommerce import views as bookcommerce_views
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', bookcommerce_views.register, name='register'),
    path('login/', bookcommerce_views.CustomLoginView.as_view(template_name='bookcommerce/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='bookcommerce/logout.html'), name='logout'),
    path('', include('bookcommerce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
