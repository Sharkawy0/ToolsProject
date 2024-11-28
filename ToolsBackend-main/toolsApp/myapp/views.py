from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
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