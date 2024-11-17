# events/urls.py
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings 
from .views import login_view, home_view, create_event_view, register_event_view, profile_view,unregister_event_view,register_view

urlpatterns = [
    path('', login_view, name='login'),
    path('home/', home_view, name='home'),
    path('create_event/', create_event_view, name='create_event'),
    path('register/', register_view, name='register'),
    path('register_event/', register_event_view, name='register_event'),
    path('profile/', profile_view, name='profile'),
    path('unregister_event/', unregister_event_view, name='unregister_event'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)