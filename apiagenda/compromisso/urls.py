from django.urls import include, path
from rest_framework import routers
from apiagenda.compromisso import views

api_router = routers.DefaultRouter()
api_router.register(r"compromisso", views.CompromissoViewSet, basename='compromissoViewset')

urlpatterns = [
    path("api/", include(api_router.urls)),
]