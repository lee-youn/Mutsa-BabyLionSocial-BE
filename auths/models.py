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
        user.description = description
        user.set_password(password)
        user.save(sing=self._db)
        return user
    def create_superuser(self, nickname, description, password=None):
        user = self.create_user(
            nickname,
            description,
            password=password
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
    
class MbtiStatus(models.Model):
    ISTJ = 'ISTJ'
    ISFJ = 'ISFJ'
    INFJ = 'INFJ'
    INTJ = 'INJJ'
    ISTP = 'ISTP'
    ISFP = 'ISFP'
    INFP = 'INFP'
    INTP = 'INTP'
    ESTJ = 'ESTJ'
    ESFJ = 'ESFJ'
    ENFJ = 'ENFJ'
    ENTJ = 'ENTJ'
    ESTP = 'ESTP'
    ESFP = 'ESFP'
    ENFP = 'ENFP'
    ENTP = 'ENTP'
    NONE = 'none', '-', 'NONE'


class MutsaUser(AbstractBaseUser):
    nickname = models.CharField(max_length=1024, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    description = models.TextField()
    age = models.IntegerField()
    mbti = models.TextChoices(max_length=128, choices=MbtiStatus.choices, default=MbtiStatus.NONE)



# Create your models here.
