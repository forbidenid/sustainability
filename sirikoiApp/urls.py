
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.shortcuts import redirect

admin.site_header = "SUSTAINABILITY"
admin.site_title = "SIRIKOI_SUSTAINABILITY"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('sustainability.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
