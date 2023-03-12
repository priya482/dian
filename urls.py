
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('', include('packages.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]

# from django.contrib import admin
# from django.urls import include, path

# urlpatterns = [
#     path('polls/', include('polls.urls')),
#     path('admin/', admin.site.urls),
# ]