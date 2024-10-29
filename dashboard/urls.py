from django.urls import path 
from .views import  *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",dashboard_index,name='dashboard_index'),
    path("dashboard_base/",dashboard_base,name='dashboard_base'),
    path("dashboard-all-customer/",dashboard_all_customer,name='dashboard-all-customer'),
    path("dashboard-add-product/",dashboard_add_product,name='dashboard-add-product'),
    path("dashboard-category/",dashboard_category,name='dashboard-category'),
    path("dashboard-all-product/",dashboard_all_product,name='dashboard-all-product'),
    path("dashboard-order/",dashboard_order,name='dashboard-order'),
    path("dashboard-calendar/",dashboard_calendar,name='dashboard-calendar'),
    path("dashboard-invoices/",dashboard_invoices,name='dashboard-invoices'),
    path("dashboard-contact/",dashboard_contact,name='dashboard-contact'),
    path("dashboard-login/",dashboard_login,name='dashboard-login'),
    path("dashboard-registration/",dashboard_registration,name='dashboard-registration'),
    path("dashboard-reset-password/",dashboard_reset_password,name='dashboard-reset-password'),
    # path("dashboard-update-password/",dashboard_update_password,name='dashboard-update-password'),
    # path("dashboard-view-profile/",dashboard_view_profile,name='dashboard-view-profile'),
    # path("dashboard-login-status/",dashboard_login_status,name='dashboard-login-status'),
    # path("dashboard-edit-profile/",dashboard_edit_profile,name='dashboard-edit-profile'),
    # path("dashboard-nestable-list/",dashboard_nestable_list,name='dashboard-nestable-list'),
    # path("dashboard-sweet-alert/",dashboard_sweet_alert,name='dashboard-sweet-alert'),
    # path("dashboard-animation/",dashboard_animation,name='dashboard-animation'),
    # path("dashboard-swiper-slider/",dashboard_swiper_slider,name='dashboard-swiper-slider'),
    # path("dashboard-utility/",dashboard_utility,name='dashboard-utility'),
    # path("dashboard-form/",dashboard_form,name='dashboard-form'),
    # path("dashboard-table/",dashboard_table,name='dashboard-table'),
    # path("dashboard-charts/",dashboard_charts,name='dashboard-charts'),
    # path("dashboard-icon/",dashboard_icon,name='dashboard-icon'),
    # path("dashboard-map/",dashboard_map,name='dashboard-map'),
    # path("dashboard-file-manager/",dashboard_file_manager,name='dashboard-file-manager'),
    path("delete_product/<int:id>/",delete_product,name='delete_product'),
    path("edit_product/<int:id>/",edit_product,name='edit-product'),
    
        
     ]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)