from django.urls import include, path
from rest_framework import routers
from apiagenda.contato.views import ContatoViewSet

api_router = routers.DefaultRouter()
api_router.register(r"contato", ContatoViewSet)

urlpatterns = [
    path("api/", include(api_router.urls)),
]
