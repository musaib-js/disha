from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name = "home"),
    path('contact/', views.contact, name = "contact"),
    path('colleges/', views.colleges, name = "colleges"),
    path('email/', views.email, name = "email"),
    path('<str:slugtwo>/', views.service, name='service'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
