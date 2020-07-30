from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #adding our new paths
    path('', include('entries.urls')),
    path('users/', include('users.urls'))
]
