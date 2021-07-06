from django.urls import path
from compromisso import views

urlpatterns = [
    path('compromisso/list', views.compromisso_list),
    path('compromisso/<int:pk>/', views.compromisso_detail),
]
