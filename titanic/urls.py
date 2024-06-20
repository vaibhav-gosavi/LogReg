from django.urls import path
from .views import predict_survival

urlpatterns = [
    path('', predict_survival, name='predict_survival'),
]
