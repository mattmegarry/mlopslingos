from django.urls import path, include
from .views import (
    LingoListApiView,
)

urlpatterns = [
    path('lingos', LingoListApiView.as_view()),
]
