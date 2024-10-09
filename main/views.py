from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.shortcuts import render, redirect, reverse   # Tambahkan import redirect di baris ini
from main.forms import ProductForm, CustomAuthenticationForm, CustomUserCreationForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags

def show_landing_page(request):
    if request.user.is_authenticated:
        return redirect('main:show_main')
    return render(request, 'landing_page.html')

@login_required(login_url='/login')
def show_main(request):
    products = Product.objects.filter(user=request.user)
    
    # Get the 'last_login' cookie, if not found, set it to None
    last_login = request.COOKIES.get('last_login', None)
    
    context= {
        'name': request.user.username,
        'class': 'PBP D',
        'products': products,
        'last_login': last_login  # This will be None if the cookie doesn't exist
    }
    return render(request, 'main.html', context)

def create_product(request):
    form = ProductForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit=False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

def edit_product(request, id):
    # Get product by id
    product = Product.objects.get(pk = id)
    
    # Set mood entry sebagai instance dari form
    form = ProductForm(request.POST or None, instance = product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def delete_product(request, id):
    # Get mood berdasarkan id
    product = Product.objects.get(pk = id)
    # Hapus mood
    product.delete()
    # Kembali ke halaman awal
    return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    else:
        form = CustomUserCreationForm()

    context = {'form': form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)  # Use the custom form
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = CustomAuthenticationForm()  # Initialize the form for GET requests

    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:show_landing_page'))
    response.delete_cookie('last_login')
    return redirect('main:show_landing_page')

@csrf_exempt
@require_POST
def add_product_entry_ajax(request):
    if request.method == "POST":
        artist_name = strip_tags(request.POST.get('artist_name'))
        album_title = strip_tags(request.POST.get('album_title'))
        price = strip_tags(request.POST.get('price'))
        description = strip_tags(request.POST.get('description'))

        # Assuming user is already logged in and request.user is available
        product = Product.objects.create(
            artist_name=artist_name,
            album_title=album_title,
            price=price,
            description=description,
            user=request.user  # Attach the product to the logged-in user
        )

        return JsonResponse({"message": "Product added successfully"}, status=201)

    return JsonResponse({"error": "Invalid request"}, status=400)
