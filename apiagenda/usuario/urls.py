from django.urls import include, path
from rest_framework import routers
from apiagenda.usuario.views import UsuarioViewSet

api_router = routers.DefaultRouter()
api_router.register(r"usuario", UsuarioViewSet)

urlpatterns = [
    path("api/", include(api_router.urls)),
]
