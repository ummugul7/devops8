from django.urls import path
from . import views

urlpatterns = [

    path('arabalar/', views.ArabaView.as_view(), name='araba-list'),
]