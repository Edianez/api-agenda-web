from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from contato import views

urlpatterns = [
    path('contato/list', views.ContatoList.as_view()),
    path('contato/<int:pk>/', views.ContatoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
