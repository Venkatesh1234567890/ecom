from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib import messages
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout,authenticate,login
from .models import Products, OrderItem  # Assuming OrderItem is your model




# Create your views here.   

def index(request):
    product= Products.objects.all()
    return render(request,'index.html',{'products':product})



def about(request):
    return render(request,'base.html')

# Add to Cart View
def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    userid  = CustomUser.objects.get(id=request.user.id)

    if request.method == "POST":
        quantity = int(request.POST.get('quantity', 1))
        weight = int(request.POST.get('weight', 1))
        total_quantity = quantity * weight
        price = product.selling_price * total_quantity
        status = 'Pending'

        order=OrderItem.objects.create(product=product,quantity=quantity,weight=weight,price = price,status = status, user_id = userid )
        messages.success(request, 'Product added to cart')
        return redirect('checkout', order_id=order.id)
        # return redirect('single_product_view', product_id=product_id)
    messages.error(request, 'Invalid request')
    return redirect('single_product_view', product_id=product_id)

    #     return JsonResponse({'message': 'Product added to cart', 'price': price})

    # return JsonResponse({'error': 'Invalid request'}, status=400)


def order_summary(request):
    order_items = OrderItem.objects.filter(status='Pending')
    order_items_dict = {
        item.id: {
            'name': item.product.title,
            'weight': item.weight,
            'quantity': item.quantity,
            'price': item.price,
            'image': item.product.images.first().image.url if item.product.images.first() else None
        }
        for item in order_items
    }
    return JsonResponse({'order_items': order_items_dict})

def delete_order(request, order_id):
    order = get_object_or_404(OrderItem, id=order_id)
    order.delete()
    messages.success(request, 'Order deleted successfully')
    return redirect('index')

def delivery(request,product_id):
    product = get_object_or_404(Products, id=product_id)
    
    if request.method == "POST":
        quantity = int(request.POST.get('quantity', 1))
        weight = int(request.POST.get('weight', 1))
        total_quantity = quantity * weight
        price = product.selling_price * total_quantity
        status = 'Pending'

        order=OrderItem.objects.create(product=product,quantity=quantity,weight=weight,price = price,status = status, user_id = request.user)


# Cart Summary View
def cart_summary(request):
    cart = request.session.get('cart', {})

    total_price = 0
    cart_items = []

    for key, item in cart.items():
        total_price += item['price'] * item['quantity']
        cart_items.append(item)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    
    return render(request, 'cart_summary.html', context)

def shop_grid(request):
    product= Products.objects.all()
    return render(request,'shop_grid.html', {'products':product})

def filter_item(request,category):
    if category == 'vegetables' or category == 'fruits':
        product= Products.objects.filter(category=category)
    elif category == 'grocery':
        product= Products.objects.filter(category=category)
    elif category == 'dairy':
        product= Products.objects.filter(category=category)
    elif category == 'beverages':
        product= Products.objects.filter(category=category)
    elif category == 'snacks':
        product= Products.objects.filter(category=category)
    elif category == 'home care':
        product= Products.objects.filter(category=category)
    elif category == 'noodles':
        product= Products.objects.filter(category=category)
    elif category == 'personal care':
        product= Products.objects.filter(category=category)
    elif category == 'pet care':
        product= Products.objects.filter(category=category)
    elif category == 'meat':
        product= Products.objects.filter(category=category)
    elif category == 'electronics':
        product= Products.objects.filter(category=category)
    else:
        product= Products.objects.all()
    return render(request,'shop_grid.html', {'products':product})


def single_product_view(request,product_id):
    product = get_object_or_404(Products, id=product_id)
    data = Products.objects.all()
    return render(request, 'single_product_view.html',{'products':product, 'datas':data})

from django.http import JsonResponse
from django.db.models import Q
from .models import Products

def ajax_search(request):
    query = request.GET.get('q', '')
    results = []

    if query:
        products = Products.objects.filter(
            Q(title__icontains=query) | Q(category__icontains=query)
        ).distinct()  # Filter by title or category

        for product in products:
            results.append({
                'id': product.id,  # Add product ID for linking
                'title': product.title,
                'selling_price': str(product.selling_price),
                'discount_price': str(product.discount_price),
                'image_url': product.images.first().image.url if product.images.exists() else None,
            })

    return JsonResponse({'results': results})


def our_blog(request):
    return render(request, 'our_blog.html')

def blog_no_sidebar(request):
    return render(request, 'blog_no_sidebar.html')

def blog_left_sidebar(request):
    return render(request, 'blog_left_sidebar.html')

def blog_right_sidebar(request):
    return render(request, 'blog_right_sidebar.html')

def blog_detail_view(request):
    return render(request, 'blog_detail_view.html')

def about_us(request):
    return render(request, 'about_us.html')


def request_product(request):
    return render(request, 'request_product.html')

def checkout(request,order_id):
    order = get_object_or_404(OrderItem, id=order_id)
    
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        address1 = request.POST.get('flat')
        address2 = request.POST.get('street')
        pincode = request.POST.get('pincode')
        city = request.POST.get('locality')
        state= request.POST.get('state')

        delivery = DeliveryAddress.objects.create(order=order,name=name,phone=phone_number,email=email,address1=address1,address2=address2,city=city,state=state,pincode=pincode)

    return render(request, 'checkout.html', {'order' : order})

def order_placed(request):
    return render(request, 'order_placed.html')

def bill(request):
    return render(request, 'bill.html')

def job_detail_view(request):
    return render(request, 'job_detail_view.html')

def sign_in(request):
    if request.method == 'POST':
        mail_id = request.POST.get('username')
        password = request.POST.get('password')

        # Authenticate with email
        user = authenticate(request, email=mail_id, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login Successful')
            return redirect('index')
        else:
            messages.error(request, 'Invalid email or password')

    return render(request, 'sign_in.html')

def sign_up(request):
    if request.method == 'POST':
        name=request.POST.get('fullname')
        email=request.POST.get('emailaddress')
        phone=request.POST.get('phone')
        password=request.POST.get('password1')
        CustomUser.objects.create_user(name=name,email=email,phone_number=phone,password=password)
        messages.success(request, 'Account created successfully')
        return redirect('sign_in')

    return render(request, 'sign_up.html')

def sign_out(request):
    logout(request)
    messages.success(request, 'Logout Successful')
    return redirect('index')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def contact_us(request):
    return render(request, 'contact_us.html')

def dashboard_overview(request):
    return render(request,'dashboard_overview.html')

def offers(request):
    return render(request,'offers.html')

def faq(request):
    return render(request,'faq.html')

def dashboard_my_orders(request):
    return render(request,'dashboard_my_orders.html')

def dashboard_my_rewards(request):
    return render(request,'dashboard_my_rewards.html')

def dashboard_my_addresses(request):
    return render(request,'dashboard_my_addresses.html')

def dashboard_my_wishlist(request):
    return render(request,'dashboard_my_wishlist.html')

def dashboard_my_wallet(request):
    return render(request,'dashboard_my_wallet.html')

def career(request):
    return render(request,'career.html')

def press(request):
    return render(request,'press.html')

def privacy_policy(request):
    return render(request,'privacy_policy.html')

def term_and_conditions(request):
    return render(request,'term_and_conditions.html')

def refund_and_return_policy(request):
    return render(request,'refund_and_return_policy.html')








