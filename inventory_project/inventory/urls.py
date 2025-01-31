from django.urls import path
from . import views

app_name = 'inventory'

urlpatterns = [
    path('', views.InventoryListView.as_view(), name='inventory_list'),
    path('add/', views.InventoryCreateView.as_view(), name='inventory_add'),
    path('edit/<int:pk>/', views.InventoryUpdateView.as_view(), name='inventory_update'),
    path('delete/<int:pk>/', views.InventoryDeleteView.as_view(), name='inventory_delete'),
    path('use/<int:pk>/', views.use_stock, name='use_stock'),
]