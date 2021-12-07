from django.contrib import admin
from django.urls import path , include
#from blogs.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls')),
    path('blogs/', include('blogs.urls')),
]
