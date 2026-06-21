from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Category, Product

def home(request):
    return render(request, 'home.html')

#category
def add_category(request):
    if request.method == "POST":
        txt1 = request.POST['txt1']
        Category.objects.create(title=txt1)
        return redirect('add_category')
    return render(request, 'add-category.html')

def display_category(request):
    categorylist = Category.objects.all()
    return render(request, 'display-category.html', {'category': categorylist})

def delete_category(request, id):
    Category.objects.get(id=id).delete()
    return redirect('display_category')

def edit_category(request, id):
    category = Category.objects.get(id=id)
    if request.method == "POST":
        category.title = request.POST['txt1']
        category.save()
        return redirect('display_category')
    return render(request, 'edit-category.html', {'category': category})

#product

def product(request):
    pdata = Product.objects.all()
    return render(request, "product.html", {'pdata': pdata})

def addproduct(request):

    if request.method == "POST":

        title = request.POST['title']
        details = request.POST['details']
        price = request.POST['price']
        category_id = request.POST['category']
        image = request.FILES['image']

        category = Category.objects.get(id=category_id)

        Product.objects.create(
            title=title,
            details=details,
            price=price,
            category=category,
            image=image
        )

        return redirect('/product')

    cdata = Category.objects.all()

    return render(request, "addproduct.html", {'cdata': cdata})


def deleteproduct(request, id):

    p = Product.objects.get(id=id)
    p.delete()

    return redirect('/product')


def editproduct(request, id):

    pdata = Product.objects.get(id=id)
    cdata = Category.objects.all()

    return render(request, "editproduct.html", {
        'pdata': pdata,
        'cdata': cdata
    })


def updateproduct(request, id):

    p = Product.objects.get(id=id)

    if request.method == "POST":

        p.title = request.POST['title']
        p.details = request.POST['details']
        p.price = request.POST['price']

        category_id = request.POST['category']
        p.category = Category.objects.get(id=category_id)

        if 'image' in request.FILES:
            p.image = request.FILES['image']

        p.save()

    return redirect('/product')





def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        messages.success(request, "Registration Successful")
        return redirect('login')

    return render(request, 'register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('user_home')
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, 'login.html')


def user_home_view(request):
    if not request.user.is_authenticated:
        return redirect('login')

    return render(request, 'user_home.html')


def logout_view(request):
    logout(request)
    return redirect('login')