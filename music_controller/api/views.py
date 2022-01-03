from .models import Room
from .serializers import RoomSerializer
from rest_framework import generics, permissions

class RoomViewSet(generics.ListCreateAPIView):
    queryset = Room.objects.all()

    permissions_class =[
        permissions.AllowAny
    ]
    serializer_class = RoomSerializer
