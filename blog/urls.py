from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import Dashboard
urlpatterns = [
    path('about/',include('about.urls')),
    path('',Dashboard.as_view(),name="my_home"),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)