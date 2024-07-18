from django.db import models
from auths.models import MutsaUser
from postt.models import Post

class Order(models.Model):
    OID = models.AutoField(primary_key=True)
    order_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=128)
    user = models.ForeignKey(MutsaUser, on_delete=models.CASCADE)
    posts = models.ManyToManyField(Post, through='PostOrder')
    

    def __str__(self):
        return f"Order {self.OID} by User {self.user.UID}"


class PostOrder(models.Model):
    post_order_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"PostOrder {self.post_order_id} with Order {self.order.OID} and Post {self.post.PID}"