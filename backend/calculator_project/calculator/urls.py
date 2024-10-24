from django.urls import path
from .views import MultiplicationView

urlpatterns = [
  path('multiply/', MultiplicationView.as_view(), name='multiply'),
]