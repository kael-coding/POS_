# pos_system/urls.py
from django.contrib import admin
from django.urls import path
from pos import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<str:name>/', views.edit_product, name='edit_product'),
    path('delete/<str:name>/', views.delete_product, name='delete_product'),  # New delete URL
    path('history/', views.history, name='history'),
    path('purchase/', views.purchase, name='purchase'),
]
