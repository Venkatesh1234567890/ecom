from django.shortcuts import render,redirect
from app.models import *

# Create your views here.


def dashboard_index(request):
    return render(request, 'dashboard_index.html')

def dashboard_base(request):
    return render(request, 'dashboard_base.html')

def dashboard_all_customer(request):
    product=Products.objects.all()

    return render(request, 'dashboard-all-customer.html',{'products':product})

def dashboard_add_product(request):
    if request.method=='POST':
        title=request.POST.get('title')
        selling_price=request.POST.get('selling')
        discount_price=request.POST.get('discount')
        category=request.POST.get('category')
        image = request.FILES.get('image')
        stock = request.POST.get('stock')
       

        product=Products.objects.create(title=title,selling_price=selling_price,discount_price=discount_price,category=category,stock=stock)

        if image:
            a = Image.objects.create(image=image)
            product.images.add(a)
            product.save()
        return redirect('dashboard-add-product')

    return render(request, 'dashboard-add-product.html')


def dashboard_category(request):
    return render(request, 'dashboard-category.html')

def dashboard_all_product(request):
    product=Products.objects.all()
    return render(request, 'dashboard-all-product.html',{'products':product})

def dashboard_order(request):
    order=OrderItem.objects.filter(status='Pending')
    
    return render(request, 'dashboard-order.html',{'orders':order})

def dashboard_calendar(request):
    return render(request, 'dashboard-calendar.html')

def dashboard_invoices(request):
    return render(request, 'dashboard-invoices.html')

def dashboard_contact(request):
    return render(request, 'dashboard-contact.html')

def dashboard_login(request):
    return render(request, 'dashboard-login.html')

def dashboard_registration(request):
    return render(request, 'dashboard-registration.html')

def dashboard_reset_password(request):
    return render(request, 'dashboard-reset-password.html')

# def dashboard_update_password(request):
#     return render(request, 'dashboard-update-password.html')

# def dashboard_view_profile(request):
#     return render(request, 'dashboard-view-profile.html')

# def dashboard_login_status(request):
#     return render(request, 'dashboard-login-status.html')

# def dashboard_edit_profile(request):
#     return render(request, 'dashboard-edit-profile.html')

# def dashboard_utility(request):
#     return render(request, 'dashboard-utility.html')

# def dashboard_sweet_alert(request):
#     return render(request, 'dashboard-sweet-alert.html')

# def dashboard_nestable_list(request):
#     return render(request, 'dashboard-nestable-list.html')

# def dashboard_animation(request):
#     return render(request, 'dashboard-animation.html')

# def dashboard_swiper_slider(request):
#     return render(request, 'dashboard-swiper-slider.html')

# def dashboard_form(request):
#     return render(request, 'dashboard-form.html')

# def dashboard_table(request):
#     return render(request, 'dashboard-table.html')

# def dashboard_charts(request):
#     return render(request, 'dashboard-charts.html')

# def dashboard_icon(request):
#     return render(request, 'dashboard-icon.html')

# def dashboard_map(request):
#     return render(request, 'dashboard-map.html')

# def dashboard_file_manager(request):
#     return render(request, 'dashboard-file-manager.html')


def delete_product(request,id):
    product=Products.objects.get(id=id)
    product.delete()
    return redirect('dashboard-all-product')

def edit_product(request,id):
    product=Products.objects.get(id=id)
   
    if request.method=='POST':
        title=request.POST.get('title')
        selling_price=request.POST.get('selling')
        discount_price=request.POST.get('discount')
        category=request.POST.get('category')
        image = request.FILES.get('image')
        stock = request.POST.get('stock')
        product.title=title
        product.selling_price=selling_price
        product.discount_price=discount_price
        product.category=category
        product.stock=stock
        if image:
            a = Image.objects.create(image=image)
            product.images.add(a)
            product.save()
        return redirect('dashboard-all-product')

    return redirect('dashboard-all-product')
    