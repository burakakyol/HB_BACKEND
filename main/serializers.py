from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('pk', 'username', 'email', 'first_name',
                  'last_name', 'date_joined', 'is_active')

class FavoriteSerializer(serializers.ModelSerializer):

    owner = serializers.Field(source='owner.username')

    class Meta:
        model = Favorite
        fields = ('id', 'start_date', 'end_date', 'title', 'desc')