from django.urls import path 
from .views import chatpage , signup 

app_name = 'chat'

urlpatterns = [
    path('' , chatpage , name = 'chat'),
    path('register/' , signup , name = 'register' ),
]