from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from compromisso import views

urlpatterns = [
    path('compromisso/list', views.CompromissoList.as_view()),
    path('compromisso/<int:pk>/', views.CompromissoDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
