from django.db import models
from auths.models import MutsaUser

class Post(models.Model):
    PID = models.AutoField(primary_key=True)
    post_title = models.CharField(max_length=255)
    content = models.TextField()
    file = models.FileField(upload_to='attachments/', null=True, blank=True)
    upload_time = models.DateTimeField(auto_now_add=True)
    expire_time = models.DateTimeField()
    user = models.ForeignKey(MutsaUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_title