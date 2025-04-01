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
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data['user']

        token, created = Token.objects.get_or_create(user=user)

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


''' create view for task completion '''

class TaskCompletionView(APIView):
    permission_classes = [TaskPermission, IsAuthenticated]

    def patch(self, request, pk):
        try:
            task = Task.objects.get(id=task_id)
        except Task.DoesNotExist:
            return Response({"error": "Task not found."}, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task, data=request.data, partial=True) #partial=True allows update only the status field
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)






