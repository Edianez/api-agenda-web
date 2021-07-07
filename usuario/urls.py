from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from usuario import views

urlpatterns = [
    path('usuario/list', views.UsuarioList.as_view()),
    path('usuario/<int:pk>/', views.UsuarioDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
