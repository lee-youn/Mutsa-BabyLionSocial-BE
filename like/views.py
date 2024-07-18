from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.request import Request
from django.http import Http404

from postt.models import Post
from auths.models import MutsaUser
from .models import Like
from .serializers import LikeSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.decorators import action

class LikeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):

    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes=[permissions.IsAuthenticated]

    # 특정 사용자의 주문 목록을 조회하여 반환
    def list(self, request: Request):
        serializer = UserSerializer(request.user) 
        user_id = serializer.data.get('id')
        
        #user_id = request.query_params.get('UID', None)
        if (user_id):
            try:
                find_member = MutsaUser.objects.get(UID=user_id)
            except MutsaUser.DoesNotExist:
                raise Http404('해당 사용자가 없습니다.')
            likes = Like.objects.filter(UID=user_id)
        else:
            likes = Like.objects.none()
        
        serializer = LikeSerializer(likes, many=True)
        return Response(serializer.data)