from rest_framework import serializers,status
from rest_framework.exceptions import APIException

from.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['PID', 'post_title', 'content', 'file', 'upload_time', 'expire_time', 'user']

    def create(self, validated_data):
        post = Post.objects.create(**validated_data)
        return post
    
    def update(self, instance, validated_data):
        instance.post_title = validated_data.get('post_title', instance.post_title)
        instance.content = validated_data.get('content', instance.content)
        instance.file = validated_data.get('file', instance.file)

        if not validated_data:
            raise NotValidatedDataException()
        
        instance.save()
        return instance
    
class NotValidatedDataException(APIException):
    status_code = status.HTTP_400_BAD_REQUEST
    default_detail = '잘못된 요청입니다.'
