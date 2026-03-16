from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny])
def register(request):
    try:
        username = request.data.get("username")
        password = request.data.get("password")
        
        if not username or not password:
            return Response({"error": "Username and password required"}, status=400)
            
        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already exists"}, status=400)

        user = User.objects.create_user(
            username=username,
            password=password
        )
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            "message": "User created",
            "token": token.key,
            "username": user.username
        }, status=201)
    except Exception as e:
        return Response({"error": str(e)}, status=500)

@csrf_exempt
@api_view(["POST"])
@permission_classes([AllowAny])
def user_login(request):
    try:
        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(username=username, password=password)

        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "message": "Login success", 
                "token": token.key,
                "username": user.username
            })

        return Response({"error": "Invalid credentials"}, status=401)
    except Exception as e:
        return Response({"error": str(e)}, status=500)
