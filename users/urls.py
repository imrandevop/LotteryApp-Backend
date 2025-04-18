from django.urls import path
from .views import SimpleRegisterView

urlpatterns = [
    path('register/', SimpleRegisterView.as_view(), name='simple-register'),
]
