from django.urls import path
from .views import login, register, dashboard, logout_view

urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('dashboard/', dashboard, name='dashboard')

]
