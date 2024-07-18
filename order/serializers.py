from rest_framework import serializers
from auths.models import MutsaUser

class PostOrderSerializer(serializers.Serializer):
    PID = serializers.IntegerField(source='post.PID')
    post_title = serializers.CharField(source='post.post_title')

class OrderSerializer(serializers.Serializer):
    UID = serializers.IntegerField(source='user.UID')
    posts = PostOrderSerializer(source='order_post_set', many=True)
    order_time = serializers.DateTimeField()
    status = serializers.CharField()      

class PostOrderRequestDTO(serializers.Serializer):
    PID = serializers.IntegerField()

class OrderRequestDTO(serializers.Serializer):
    UID = serializers.IntegerField()
    posts = PostOrderRequestDTO(many=True)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MutsaUser
        fields = '__all__'