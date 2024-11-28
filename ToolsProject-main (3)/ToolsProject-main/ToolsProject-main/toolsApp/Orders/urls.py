from django.urls import path
from .views import CreateOrderView, MyOrdersView, OrderDetailsView, CancelOrderView, AssignedOrdersToCourierView

urlpatterns = [
    path('create-order/', CreateOrderView.as_view(), name='create_order'),
    path('my-orders/', MyOrdersView.as_view(), name='my_orders'),
    path('order-details/<int:order_id>/', OrderDetailsView.as_view(), name='order_details'),
    path('cancel-order/<int:order_id>/', CancelOrderView.as_view(), name='cancel_order'),
    path('assigned-orders/', AssignedOrdersToCourierView.as_view(), name='assigned_orders'),
]