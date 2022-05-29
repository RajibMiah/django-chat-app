from argparse import Namespace
from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from chat.views  import logout_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('logout/' , logout_view , name = 'logout'),
    path('chat/' , include('chat.urls') , name = 'chat'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)