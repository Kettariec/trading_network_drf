from rest_framework import serializers
from user.models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор пользователя"""
    password = serializers.CharField(min_length=8, write_only=True)

    def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ('id', 'email', 'password',
                  'phone', 'country', 'city', 'avatar')