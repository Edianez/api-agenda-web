from django.urls import include, path
from rest_framework import routers
from apiagenda.compromisso.views import CompromissoViewSet

api_router = routers.DefaultRouter()
api_router.register(r"compromisso", CompromissoViewSet)

urlpatterns = [
    path("api/", include(api_router.urls)),
]