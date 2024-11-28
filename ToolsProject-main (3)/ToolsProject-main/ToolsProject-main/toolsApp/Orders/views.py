from django.http import JsonResponse
from django.views import View
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.views.decorators.csrf import ensure_csrf_cookie
from jupyter_lsp.specs import json

# In-memory data storage
orders = []
order_id_counter = 1  # Simple counter for order IDs


class CreateOrderView(View):
    def post(self, request):
        global order_id_counter
        data = json.loads(request.body)
        new_order = {
            "id": order_id_counter,
            "user": data['user'],
            "order_details": data['order_details'],
            "status": "Pending"
        }
        orders.append(new_order)
        order_id_counter += 1
        return JsonResponse(new_order, status=201)

class MyOrdersView(View):
    def get(self, request):
        user = request.GET.get('user')  # Get user from query parameters
        user_orders = [order for order in orders if order['user'] == user]
        return JsonResponse(user_orders, safe=False)


class OrderDetailsView(View):
    def get(self, request, order_id):
        order = next((order for order in orders if order['id'] == order_id), None)
        if order:
            return JsonResponse(order)
        return JsonResponse({'error': 'Order not found'}, status=404)


class CancelOrderView(View):
    def post(self, request, order_id):
        global orders
        order = next((order for order in orders if order['id'] == order_id), None)
        if order and order['status'] == "Pending":
            orders.remove(order)
            return JsonResponse({'message': 'Order cancelled successfully'})
        return JsonResponse({'error': 'Order not found or cannot be cancelled'}, status=404)


class AssignedOrdersToCourierView(View):
    def get(self, request):
        # This will just return all orders for simplicity
        return JsonResponse(orders, safe=False)