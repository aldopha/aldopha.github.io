from week10project import views
from django.urls import path

urlpatterns = [
    path("", views.home),
    path("ccu411315051", views.ccu411315051)
]
