from django.conf.urls import include
from django.urls import path

urlpatterns = [
    path("api/v1/", include("ebau-gwr.core.urls"),),
]