from rest_framework import serializers
from auths.models import MutsaUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MutsaUser
        fields = '__all__'

class UserLogoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = MutsaUser
        fields = '__all__'