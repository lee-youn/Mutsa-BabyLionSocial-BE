from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class MutsaUserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, nickname, description, password=None):
        if not nickname:
            raise ValueError('User must have a nickname')
        
        user = self.model(
            nickname=nickname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, nickname, description, password=None):
        user = self.create_user(
            nickname,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
# class MbtiStatus(models.TextChoices):
#     ISTJ = 'ISTJ', 'ISTJ'
#     ISFJ = 'ISFJ', 'ISFJ'
#     INFJ = 'INFJ', 'INFJ'
#     INTJ = 'INTJ', 'INTJ'
#     ISTP = 'ISTP', 'ISTP'
#     ISFP = 'ISFP', 'ISFP'
#     INFP = 'INFP', 'INFP'
#     INTP = 'INTP', 'INTP'
#     ESTJ = 'ESTJ', 'ESTJ'
#     ESFJ = 'ESFJ', 'ESFJ'
#     ENFJ = 'ENFJ', 'ENFJ'
#     ENTJ = 'ENTJ', 'ENTJ'
#     ESTP = 'ESTP', 'ESTP'
#     ESFP = 'ESFP', 'ESFP'
#     ENFP = 'ENFP', 'ENFP'
#     ENTP = 'ENTP', 'ENTP'
#     NONE = 'none', 'NONE'


class MutsaUser(AbstractBaseUser):
    nickname = models.CharField(max_length=1024, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    school = models.CharField(max_length=1024, default= "-")
    login = models.BooleanField(default=True)

    objects = MutsaUserManager()

    USERNAME_FIELD = 'nickname'

    @property
    def is_staff(self):
        return self.is_admin


# Create your models here.
