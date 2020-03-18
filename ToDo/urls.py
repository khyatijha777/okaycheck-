'''import'''
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('accounts/', include('accounts.urls')),
    # path('calendar', include('todo_calendar.urls')),
    path('gallery/', include('gallery.urls')),
    path('profile/', include('user_profile.urls')),
]
