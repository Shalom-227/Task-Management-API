from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from . import views

from rest_framework.routers import DefaultRouter


'''creating a router and registering the viewset'''
router = DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename='task')



urlpatterns = [       
    #creates token endpoint
    path('api/token-auth/', obtain_auth_token, name = 'api-token-auth'),

    #creates endpoints for authentication
    path('api/users/register/', views.RegisterView.as_view(), name = 'register'),
    path('api/users/login/', views.LoginView.as_view(), name = 'login'),
    path('api/users/logout/', views.LogoutView.as_view(), name = 'logout'),
    

    #create endpoints for task operations
    path('api/', include(router.urls)),
    path('api/tasks/<int:pk>/complete/', views.TaskCompletionView.as_view(), name='task-complete'),



        ]


