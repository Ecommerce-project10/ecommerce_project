<<<<<<< HEAD
from django.contrib import admin
from django.urls import path ,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
=======
from django.urls import path,include

urlpatterns = [
path('cart/', include('cart.urls')),

>>>>>>> 792ab0b (add cart and checkout pages)
]
