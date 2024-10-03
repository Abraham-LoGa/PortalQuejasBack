from models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerialzer):
    class Meta:
        model = User
        fields = '__all__'