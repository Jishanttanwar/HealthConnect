from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True , min_length = 8)

    class Meta():
        model = User
        fields = (
            "email",
            "username",
            "password",
            "phone_number",
            'role',
        )
    def create(self , validated_data):
        password = validated_data.pop("password")
        user = User.objects.create_user(password=password , **validated_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta():
        model = User
        fields = (
            "id",
            "email",
            "username",
             "phone_number",
             "role",
             "is_verified",
             "created_at",
        )