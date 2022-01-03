from rest_framework import serializers
from api.models import Room

# Room serializers
class RoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Room
        fields ='__all__'                     #('id', 'code', 'host', 'guest_can_pause', 'votes_to_skip', 'created_at')