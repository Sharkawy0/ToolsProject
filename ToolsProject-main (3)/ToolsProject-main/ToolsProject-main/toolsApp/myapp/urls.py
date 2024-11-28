from django.urls import path

from . import views
from .views import test

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('courier/orders/<int:courier_id>/', views.assigned_orders, name='assigned_orders'),
    path('courier/order/<int:order_id>/<str:action>/', views.update_order_acceptance, name='update_order_acceptance'),
     path('courier/order/status/', views.update_order_status, name='update_order_status'),
    path('test/',test, name='test')
]
