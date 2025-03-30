from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from .serializers import RegisterSerializer, LoginSerializer, TaskSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.viewsets import ModelViewSet
from .models import Task


# Create your views here.

''' view for user registration '''
class RegisterView(CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({"message": "User registered successfully."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

''' view for user login '''
class LoginView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_created(user=user)

        return Response({
            'token': token.key,
            'username': user.username,
            'message': 'Login successful',
            }, status=status.HTTP_200_OK)


''' view for user logout'''
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        token = request.auth
        if token:
            token.delete()
            return Response({"message": "Successfully logged out."}, status=status.HTTP_200_OK)
        return Response({"error": "No active token found."}, status=status.HTTP_400_BAD_REQUEST)


'''create custom permission for Task viewset'''
class TaskPermission(IsAuthenticatedOrReadOnly):

    def has_permission(self, request, view):
        if request.method == 'POST' and view.action == 'login':
            return True
        return super().has_permission(request, view)

class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [TaskPermission, IsAuthenticated]






