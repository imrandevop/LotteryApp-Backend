from rest_framework import serializers
from .models import CustomUser

class SimpleRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'user_id']
        read_only_fields = ['user_id']

    def create(self, validated_data):
        return CustomUser.objects.create(username=validated_data['username'])
