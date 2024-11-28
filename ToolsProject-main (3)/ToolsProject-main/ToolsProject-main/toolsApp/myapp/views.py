from django.contrib.admin import action
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import  HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Order, Courier
import json

def test(request):
    return HttpResponse('shaghal!')

# User Registration View
@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')

        if not username or not email or not password:
            return HttpResponse({'error : Missing fields'}, status=400)

        if User.objects.filter(email=email).exists():
            return HttpResponse({'error : Email already in use'}, status=400)

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        return HttpResponse({'message : User registered successfully'}, status=201)

# User Login View
@csrf_exempt
def user_login(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return HttpResponse({'error : User not found'}, status=404)

        user = authenticate(username=user.username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponse({'message : Login successful'}, status=200)
        else:
            return HttpResponse({'error : Invalid credentials'}, status=401)


@csrf_exempt
def update_order_status(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        order_id = data.get('order_id')
        new_status = data.get('new_status')
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return HttpResponse({'order_status': 'error', 'message': 'Order not found'}, status=404)

        valid_statuses = [option[0] for option in Order.STATUS_OPTIONS]
        if new_status not in valid_statuses:
            return HttpResponse({'order_status': 'error', 'message': 'Invalid status'}, status=400)

        order.order_status = new_status
        order.save()
        return HttpResponse({'status': 'success', 'new_status': order.order_status})

def assigned_orders(request, courier_id):
    orders = Order.objects.filter(courier_id=courier_id)
    list_of_order = [{
        'order_id': order.id,
        'status': order.order_status,
        'pickup_location': order.pickup_location,
        'delivery_location': order.delivery_location
    } for order in orders]
    return HttpResponse(list_of_order, safe=False)


def update_order_acceptance(request, order_id, action):
    try:
        order = Order.objects.get(id=order_id)
        # Update the order's status based on the action
        if action == 'accept':
            order.order_status = 'accepted'
        elif action == 'decline':
            order.order_status = 'declined'
        else:
            return HttpResponse({'error': 'Invalid action'}, status=400)
        order.save()
        return HttpResponse({'success': True, 'new_status': order.order_status})

    except Order.DoesNotExist:
        return HttpResponse({'error': 'Order is not found'}, status=404)


def get_assigned_orders(request):
    courier_id = request.GET.get('courier_id')

    # Filter orders by courier if courier_id is provided, otherwise get all orders
    orders = Order.objects.filter(courier_id=courier_id) if courier_id else Order.objects.all()

    data = [
        {
            'id': order.id,
            'status': order.order_status,
            'courier': order.courier.name if order.courier else "Unassigned",
            'created_at': order.created_at
        } for order in orders
    ]
    return HttpResponse({'orders': data})


def reassign_order(request, order_id):
    try:
        courier_id = request.GET.get('courier_id')
        order = Order.objects.get(id=order_id) # get the specified order

        # If a courier ID is provided, attempt to fetch the new courier and reassign
        if courier_id: # if a courier ID is provided
            new_courier = Courier.objects.get(id=courier_id)
            order.courier = new_courier
        else:
            order.courier = None  # Unassign if no courier ID is provided

        order.save()  # Save the updated order assignment
        return HttpResponse({'success': True, 'new_courier': order.courier.name if order.courier else "Unassigned"})

    except Order.DoesNotExist:
        return HttpResponse({'error': 'Order not found'}, status=404)
    except Courier.DoesNotExist:
        return HttpResponse({'error': 'Courier not found'}, status=404)