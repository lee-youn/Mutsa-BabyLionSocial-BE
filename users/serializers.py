from rest_framework import serializers
from auths.models import MutsaUser

class UserSerializer(serializers.Serializer):
    class Mets:
        model = MutsaUser
        fields = ['id','nickname','description','age','mbti']

class UserLogoutSerializer(serializers.Serializer):
    class Mets:
        model = MutsaUser
        fields = '__all__'