from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.request import Request
from django.http import Http404

from postt.models import Post
from auths.models import MutsaUser
from order.models import Order, PostOrder
from order.serializers import OrderRequestDTO, OrderSerializer, UserSerializer

class OrderViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet):

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # 특정 사용자의 주문 목록을 조회하여 반환
    def list(self, request: Request):
        serializer = UserSerializer(request.user) 
        user_id = serializer.data.get('id')
        if (user_id):
            try:
                find_member = MutsaUser.objects.get(UID=user_id)
            except MutsaUser.DoesNotExist:
                raise Http404('해당 사용자가 없습니다.')
            orders = Order.objects.filter(UID=user_id)
        else:
            orders = Order.objects.none()
        
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
    
    def create(self, request):
        # 요청 데이터를 OrderRequestDTO 시리얼라이저를 사용하여 검증함.
        serializer = OrderRequestDTO(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        try:
            user = MutsaUser.objects.get(id=data['UID'])
        except MutsaUser.DoesNotExist:
            raise ValidationError('해당 유저가 없습니다.')
        
        order = Order(UID=user)
        order_posts = []
        posts = []
        for order_post_data in data['posts']:
            try:
                post = Post.objects.get(id=order_post_data['PID'])
            except:
                raise ValidationError('해당 게시글이 없습니다.')
            
            posts.append(post)
            order_posts.append(PostOrder(
                    order=order,
                    post=post))
            order.save()
        for order_post in order_posts:
            order_post.save()
        for post in posts:
            post.save()

        serializer = OrderSerializer(order)
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
        except:
            raise Http404('해당 구매가 없습니다.')

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        instance.status = "구매 취소"
        instance.save()

        serializer = OrderSerializer(instance)
        return Response(serializer.data) 
