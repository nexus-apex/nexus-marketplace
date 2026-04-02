from django.urls import path
from . import views

urlpatterns = [
    path('', lambda r: views.redirect('/dashboard/')),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('marketstores/', views.marketstore_list, name='marketstore_list'),
    path('marketstores/create/', views.marketstore_create, name='marketstore_create'),
    path('marketstores/<int:pk>/edit/', views.marketstore_edit, name='marketstore_edit'),
    path('marketstores/<int:pk>/delete/', views.marketstore_delete, name='marketstore_delete'),
    path('marketproducts/', views.marketproduct_list, name='marketproduct_list'),
    path('marketproducts/create/', views.marketproduct_create, name='marketproduct_create'),
    path('marketproducts/<int:pk>/edit/', views.marketproduct_edit, name='marketproduct_edit'),
    path('marketproducts/<int:pk>/delete/', views.marketproduct_delete, name='marketproduct_delete'),
    path('marketorders/', views.marketorder_list, name='marketorder_list'),
    path('marketorders/create/', views.marketorder_create, name='marketorder_create'),
    path('marketorders/<int:pk>/edit/', views.marketorder_edit, name='marketorder_edit'),
    path('marketorders/<int:pk>/delete/', views.marketorder_delete, name='marketorder_delete'),
    path('settings/', views.settings_view, name='settings'),
    path('api/stats/', views.api_stats, name='api_stats'),
]
