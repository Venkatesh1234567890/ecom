from django.urls import path 
from .views import  *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",index,name='index'),
    path("about/",about,name='base'),
    path("shop_grid/",shop_grid,name='shop_grid'),
    path("shop_grid/<str:category>/",filter_item,name='filter_item'),
    path('our_blog/', our_blog, name='our_blog'),
    path('blog_no_sidebar/', blog_no_sidebar, name='blog_no_sidebar'),
    path('blog_left_sidebar/', blog_left_sidebar, name='blog_left_sidebar'),
    path('blog_right_sidebar/', blog_right_sidebar, name='blog_right_sidebar'),
    path('blog_detail_view/', blog_detail_view, name='blog_detail_view'),
    path('about_us/', about_us, name='about_us'),
    path('single_product_view/<int:product_id>', single_product_view, name='single_product_view'),
    path('checkout/<int:order_id>/', checkout, name='checkout'),
    path('request_product/', request_product, name='request_product'),
    path('order_placed/', order_placed, name='order_placed'),
    path('bill/', bill, name='bill'),
    path('job_detail_view/', job_detail_view, name='job_detail_view'),
    path('sign_in/', sign_in, name='sign_in'),
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_out/', sign_out, name='sign_out'),
    path('forgot_password/', forgot_password, name='forgot_password'),
    path('contact_us/', contact_us, name='contact_us'),
    path('dashboard_overview/',dashboard_overview,name='dashboard_overview'),
    path('offers/', offers, name='offers'),
    path('faq/', faq, name='faq'),
    path('dashboard_my_orders/', dashboard_my_orders, name='dashboard_my_orders'),
    path('dashboard_my_rewards/', dashboard_my_rewards, name='dashboard_my_rewards'),
    path('dashboard_my_addresses/', dashboard_my_addresses, name='dashboard_my_addresses'),
    path('dashboard_my_wishlist/', dashboard_my_wishlist, name='dashboard_my_wishlist'),
    path('dashboard_my_wallet/', dashboard_my_wallet, name='dashboard_my_wallet'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('career/', career, name='career'),
    path('press/', press, name='press'),
    path('privacy_policy/', privacy_policy, name='privacy_policy'),
    path('term_and_conditions/', term_and_conditions, name='term_and_conditions'),
    path('refund_and_return_policy/', refund_and_return_policy, name='refund_and_return_policy'),
    path('order_summary/', order_summary, name='order_summary'),
    path('delete_order/<int:order_id>/', delete_order, name='delete_order'),
    path('ajax_search/', ajax_search, name='ajax_search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)