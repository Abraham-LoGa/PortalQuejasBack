from rest_framework import serializers
from api.models import Comment, Complaints
from django.contrib.auth.hashers import make_password
class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'

class ComplaintsSerializer(serializers.ModelSerializer):

    comments = CommentSerializer(many=True, read_only=True)
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Complaints
        fields = '__all__'

    def create(self, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data['password'])
        return super().create(validated_data)