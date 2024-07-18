from django.db import models
from auths.models import MutsaUser
from postt.models import Post

class Like(models.Model):
    LID = models.AutoField(primary_key=True)
    like_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(MutsaUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"Like {self.LID} on Post {self.post.PID} by User {self.user.UID}"