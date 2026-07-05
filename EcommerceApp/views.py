from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from .forms import *
from django.db.models import Q



#--------------------------------Dashboard----------------------------------


def DashboardPage(request):
    return render(request, 'pages/dashboard.html')




#--------------------------------Authentication----------------------------------


def RegisterPage(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Register Successful')
            return redirect('login')
    else:
        form=RegisterForm()
    cont={'form':form}
    return render(request, 'auth/register.html',cont)



def LoginPage(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!!')
            return redirect('dashboard')
    else:
        form =AuthenticationForm()
    cont={'form': form}
    return render(request, 'auth/login.html', cont)


def LogoutPage(request):
    logout(request)
    messages.info(request, 'You are logged out!!!')
    return redirect('dashboard')




#--------------------------------Profile----------------------------------

def AdminProfilePage(request):
    try:
        admin_profile=AdminModel.objects.get(user=request.user)
    except AdminModel.DoesNotExist:
        admin_profile = None

    if request.method == 'POST':
        aform = AdminForm(request.POST, instance=admin_profile)
        if aform.is_valid():
            profile=aform.save(commit=False)
            profile.user=request.user
            profile.save()
            messages.success(request, 'Profile Updated')
            return redirect('profile')
    else:
        aform = AdminForm(instance=admin_profile)
    cont={'aform': aform}
    return render(request, 'pages/createprofile.html', cont)

def CustomerProfilePage(request):
    try:
        customer_profile = CustomerModel.objects.get(user=request.user)
    except CustomerModel.DoesNotExist:
        customer_profile= None

    if request.method == 'POST':
        cform= CustomerForm(request.POST, instance=customer_profile)
        if cform.is_valid():
            profile=cform.save(commit=False)
            profile.user= request.user
            profile.save()
            messages.success(request, 'Profile Updated')
            return redirect('profile')
    else:
        cform=CustomerForm(instance=customer_profile)
    cont={'cform':cform}
    return render(request, 'pages/createprofile.html', cont)


def ProfilePage(request):
    if request.user.user_type == 'admin':
        try:
            data=AdminModel.objects.get(user=request.user)
        except AdminModel.DoesNotExist:
            data =None
    
    else:
        try:
            data=CustomerModel.objects.get(user=request.user)
        except CustomerModel.DoesNotExist:
            data=None

    cont={'data':data}   

    return render(request, 'pages/profile.html', cont)





#--------------------------------Category----------------------------------


def categorypage(request):
    if request.method == 'POST':
        form=CategoryForm(request.POST)
        if form.is_valid():
            cate=form.save(commit=False)
            cate.name = cate.name.lower()

            if CategoryModel.objects.filter(name=cate.name).exists():
                messages.error(request, 'Category Already Exists')
                return redirect('category')
            else:
                cate.save()
                messages.success(request, 'Category Added Successfully')
                return redirect('category')
    else:
        form=CategoryForm()
    data=CategoryModel.objects.all()

    search=request.GET.get('search')
    if search:
        data=CategoryModel.objects.filter(
            Q(name__icontains = search)
        )

    count=data.count()
    cont={'form': form, 'data':data, 'count':count}
    return render(request, 'pages/category.html', cont)



def categoryEditpage(request,id):
    data=CategoryModel.objects.get(id=id)
    if request.method == 'POST':
        form=CategoryForm(request.POST, instance=data)
        if form.is_valid():
            cate=form.save(commit=False)
            cate.name=cate.name.lower()

            if CategoryModel.objects.filter(name=cate.name).exclude(id=id).exists():
                messages.error(request, 'Category Already Exists')
            else:
                cate.save()
                messages.success(request, 'Category Updated Successfully')
                return redirect('category')
    else:
        form=CategoryForm(instance=data)
    cont={'form': form,'data':data}
    return render(request, 'pages/editcategory.html', cont)


def CategoryDeletePage(request,id):
    CategoryModel.objects.get(id=id).delete()
    messages.warning(request, 'Category Deleted!!')
    return redirect('category')






#--------------------------------Product----------------------------------


def ProductPage(request,id=None):
    try:
        data=ProductModel.objects.get(id=id)
    except ProductModel.DoesNotExist:
        data=None

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=data)
        if form.is_valid():
            product=form.save(commit=False)
            product.admin=request.user
            product.save()

            if id:
                messages.success(request, 'Product Updated Successfully')
            else:
                messages.success(request, 'Product Added Successfully')
            return redirect('product')
    else:
        form = ProductForm(instance=data)

    cdata = CategoryModel.objects.all()
    all_data = ProductModel.objects.all()

    filter_data=request.GET.get('filter_data')
    search= request.GET.get('search')

    if filter_data:
        all_data= ProductModel.objects.filter(category_id=filter_data)
    
    if search:
        all_data=ProductModel.objects.filter(
            Q(name__icontains = search)|
            Q(description__icontains = search)|
            Q(category__name__icontains = search)
        )


    
    count = all_data.count()
    cont={'form':form, 'all_data':all_data, 'count': count, 'cdata': cdata, 'filter_data': filter_data,  'is_edit':True}
    return render(request, 'pages/product.html', cont)



def ProductDeletePage(request,id):
    ProductModel.objects.get(id=id).delete()
    messages.warning(request, 'Product Deleted!!')
    return redirect('product')










# Create your views here.
