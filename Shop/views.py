from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, SignUp
from cart.forms import CartAddProductForm
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegister
from django.contrib.auth.decorators import login_required


# the homepage of the website for the list of the major products the customers
def product_list(request):
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    latest = Product.objects.order_by('-created_at')[0:3]
    #wo = Product.objects.filter(category="foot wear")
    # create a filter that collects all the items under mens wear in one section
    if request.method =="POST":
        email = request.POST["email"]
        new_signup = SignUp()
        new_signup.email = email
        new_signup.save()
        
    context = {
        'latest': latest,
        'categories': categories,
        'products': products
    }
    return render(request, 'Shop/list.html', context)


def product_detail(request, id):
    product = Product.objects.get(id= id)
    cart_product_form = CartAddProductForm()
    categories = Category.objects.all()
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
        'categories': categories,
    }
    return render(request, 'Shop/detail.html', context)

# fucntion for the searching of the store
def search(request):
    categories = Category.objects.all()
    queryset = Product.objects.all()
    query = request.GET.get("q")
    if query:
        queryset = queryset.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query)
        ).distinct()

        context = {
            'categories': categories,
            'queryset': queryset
        }
    return render(request, "Shop/search.html", context)


def register(request):
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect("Login")
    else:
        form = UserRegister()

    context = {
        'form':form,
    }

    return render(request, "Shop/register.html", context)



def login(request):
    return render(request, "Shop/login.html")


# views for the various sections of categories that are in the store
def men(request):
    query = Product.objects.filter(search='men')
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'query': query
    }
    return render(request, "Shop/cat.html", context)

def watch(request):
    query = Product.objects.filter(search='watch')
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'query': query
    }
    return render(request, "Shop/cat.html", context)

def ladies(request):
    query = Product.objects.filter(search='women')
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'query': query
    }
    return render(request, "Shop/cat.html", context)

def bags(request):
    query = Product.objects.filter(search='bags')
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'query': query
    }
    return render(request, "Shop/cat.html", context)

def kids(request):
    query = Product.objects.filter(search='kids')
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'query': query
    }
    return render(request, "Shop/cat.html", context)

def shoes(request):
    query = Product.objects.filter(search='shoes')
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'query': query
    }
    return render(request, "Shop/cat.html", context)