from django.urls import path
from .views import (
    LingoApiView
)

urlpatterns = [
    path('', LingoApiView.as_view()),
]
