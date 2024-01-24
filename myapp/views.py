from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from .forms import CustomUserCreationForm
from .models import Client
from .models import Client, Company, Product, Sales
from .forms import CompanyForm, ProductForm, SalesForm, ClientForm

def home_index(request):
    return render(request,'myapp/index.html')

def dashboard_view(request):
    username = request.user.username
    sales = Sales.objects.all()
    products = Product.objects.all()
    return render(request,'myapp/dashboard/dashboard.html',  {'username': username, 'sales': sales, 'products': products})

def charts_view(request):
    username = request.user.username
    sales = Sales.objects.all()
    products = Product.objects.all()
    return render(request,'myapp/dashboard/charts.html', {'username': username,'sales': sales, 'products': products})

def tables_view(request):
    username = request.user.username
    sales = Sales.objects.all()
    products = Product.objects.all()
    
    return render(request,'myapp/dashboard/tables.html', {'username': username,'sales': sales, 'products': products})

def insert(request):
    username = request.user.username
    companies = Company.objects.all()
    products = Product.objects.all()
    return render(request, 'myapp/dashboard/insert.html', {'username': username,'companies': companies, 'products': products})

def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)
        if form.is_valid():
            company_name = form.cleaned_data['name']

            # Check if a company with the same name already exists
            existing_company = Company.objects.filter(name=company_name).exists()

            if not existing_company:
                form.save()
                messages.success(request, "Company inserted successfully!")
                return redirect('myapp:insert')
            else:
                messages.error(request, "Company with this name already exists.")
    else:
        form = CompanyForm()

    return redirect('myapp:insert')

def create_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product_name = form.cleaned_data['name']
            product_company_id = form.cleaned_data['c_id'].id  # Assuming the foreign key is named 'company'

            # Check if a product with the same name already exists for the same company
            existing_product = Product.objects.filter(name=product_name, c_id=product_company_id).exists()

            if not existing_product:
                form.save()
                messages.success(request, "Product inserted successfully!")
                return redirect('myapp:insert')  # Redirect to the product list view
            else:
                messages.error(request, "Product with this name already exists for the selected company.")
    else:
        form = ProductForm()

    return redirect('myapp:insert')

def create_sales(request):
    if request.method == 'POST':
        form = SalesForm(request.POST, request.FILES)
        form2 = SalesForm(request.POST)
        if form.is_valid():
                form.save()
                messages.success(request, "Sales inserted successfully!")
                return redirect('myapp:insert') 
    else:
        form = SalesForm()

    return redirect('myapp:insert')

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Create a Client instance and associate it with the user
            Client.objects.create(
                user=user,
                email=user.email,
                password=user.password,
            )

            login(request, user)
            return redirect('/dashboard')
        else:
            print(form.errors)
        
    else:
        form = CustomUserCreationForm()

    return render(request, 'myapp/signup.html', {'form': form})

    # if request.method == 'POST':
    #     form = SignUpForm(request.POST)
    #     if form.is_valid():
    #         username = form.cleaned_data['username']
    #         email = form.cleaned_data['email']
    #         pass1 = form.cleaned_data['password1']
    #         pass2 = form.cleaned_data['password2']

    #         if pass1!=pass2:
    #             messages.success(request, ("Your password doesnot match"))
    #             return redirect('/signup')

    #         my_user = User.objects.create_user(username, email, pass1)

    #         try:
    #             validate_password(pass1, user=my_user)
    #             my_user.save()

    #         except ValidationError as e:
    #             my_user.delete()  # Rollback user creation
    #             messages.error(request, e)
    #             return redirect('/signup')

    #         messages.success(request, ("Account Registered Successfully!"))
    #         return redirect('/login')
    #     else:
    #         messages.error(request, "Form is not valid. Please correct the errors.")
    #         return redirect('/signup')
    # else:
    #     form = SignUpForm()
    # return render(request, 'myapp/signup.html', {'form': form})
# f"Welcome, {user.username}!"

def log_in(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            # messages.success(request, ("Login Successfully!"))
            return redirect('/dashboard')
        else:
            messages.error(request, "Invalid login credentials. Please try again.")
            return render(request, 'myapp/login.html', {'entered_email': email})

    return render(request, 'myapp/login.html')


def log_out(request):
    logout(request)
    return redirect(('/'))
