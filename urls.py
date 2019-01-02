from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Pastebin API')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rental/', include('Rental.urls')),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^$', schema_view)
]
