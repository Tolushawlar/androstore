"""Pentos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from Shop import views
from django.contrib.auth import views as auth_views

app_name = "Shop"

urlpatterns = [
    path('admin/', admin.site.urls),
    #for the cart application 
    path('cart/', include('cart.urls')),
    # for the orders application 
    path('orders/', include('orders.urls')),
    # for the main homepage of the shop appication 
    path('', views.product_list, name="ProductList"),
    # for the register page of the shop application
    path('register/', views.register, name="Register"),
    # for the login page of the shop appication 
    path('accounts/login/', auth_views.LoginView.as_view(template_name="Shop/login.html"), name="Login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name="Shop/logout.html"), name="Logout"),
    # for the details of the products in the shop appication
    path('pentos/<int:id>/', views.product_detail, name="ProductDetails"),
    #for the searching of the store
    path('search/', views.search, name="Search"),

    # for the views for the various categories that in the store
    path('category/men/', views.men, name="Men"),
    path('category/watch/', views.watch, name="Watch"),
    path('category/ladies/', views.watch, name="Ladies"),
    path('category/kids/', views.watch, name="Kids"),
    path('category/bags/', views.watch, name="Bags"),
    path('category/shoes/', views.watch, name="Shoes"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""

ath('books/details/<int:id>/', views.bookShowDetail, name="book-show-detail"),
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
    """
