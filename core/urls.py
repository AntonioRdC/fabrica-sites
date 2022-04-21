from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('detalhar_servicos/<int:pk>/', views.ServicosView.as_view(),
         name='detalhar_servicos')
]
