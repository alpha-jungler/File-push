from django.urls import path
from . import views
from django.contrib import admin
from django.urls import include, path
urlpatterns = [
    path('members/', views.members, name='members'),
]
urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]