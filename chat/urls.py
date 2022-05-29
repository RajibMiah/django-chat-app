from django.urls import path 
from .views import home ,room ,chatpage , signup

app_name = 'chat'

urlpatterns = [
    path('', home , name= 'home' ),
    path('register/' , signup , name = 'register' ),
    path('chat/' , chatpage , name = 'chatpage'),
    path('<str:room_name>/', room, name='room'),
]