from django.urls import path
from . import views

urlpatterns = [
    path('api/room/', views.RoomViewSet.as_view()),
]