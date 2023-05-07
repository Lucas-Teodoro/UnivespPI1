from django.urls import path
from . import views

urlpatterns = [
    path('',views.menutca, name='menutca'),
    path('cadastrartca/', views.cadastrartca, name='cadastrartca'),
    path('listartca/',views.listartca, name='listartca'),
]
