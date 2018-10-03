from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('main.urls')),
	path('jobs/', include('jobs.urls')),
	path('interviews/', include('interviews.urls')),
    path('admin/', admin.site.urls),
]