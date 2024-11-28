from django.urls import path

from . import views
from .views import register, user_login, test , CreateOrderView, MyOrdersView, OrderDetailsView, CancelOrderView, AssignedOrdersToCourierView

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('test/',test, name='test')
]
