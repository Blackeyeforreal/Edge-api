from django.db import models

from django.db.models.aggregates import Max
from django.utils import timezone
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


# Create your models here.
# Create your models here.

class CricketTeam(models.Model):
    id = models.AutoField(primary_key= True)
    teamName = models.CharField(max_length= 23)
    teamImage = models.ImageField()
    userImage = models.CharField(max_length= 23 )
    userToken = models.UUIDField()
    userRegion = models.CharField(max_length = 50)

class CricketPlayer(models.Model):
    Name = models.CharField(max_length=34)
    id = models.AutoField(primary_key=True)
    age = models.PositiveIntegerField(max_length=90) # 17+ (1 year ingame is 90 days in real life)
    handed  = models.CharField(max_length=8)  #left/right
    bowlingtype  = models.CharField(max_length=10) #fast / medium /off spin / leg spin
    battingVspin  = models.PositiveIntegerField(max_length=30)#: 0 to 20
    battingVpace = models.PositiveIntegerField(max_length=30)#: 0 to 20
    bowling = models.PositiveIntegerField(max_length=30)#: 0 to 20
    experience = models.PositiveIntegerField(max_length=30)#: 0 to 20
    fielding = models.PositiveIntegerField(max_length=30)#: 0 to 20
    TeamId = models.ForeignKey("CricketTeam" , on_delete = models.CASCADE)
    region = models.CharField(max_length= 34)





class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')

        now = timezone.now()
        user = self.model(
            email=self.normalize_email(email),
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            joined_at=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def get_by_natural_key(self, username):
        return self.get(**{'{}__iexact'.format(self.model.USERNAME_FIELD): username})

    def create_user(self, email, password, **extra_fields):
        return self._create_user(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class Users (AbstractBaseUser, PermissionsMixin):
    #name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    email = models.EmailField('Email', max_length=255,unique=True)
    name = models.CharField('Name', max_length=255, blank=True)
    is_staff = models.BooleanField('Is staff', default=False)
    is_active = models.BooleanField('Is active', default=True)
    joined_at = models.DateTimeField('Joined at', default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    # def __str__(self):
    #     return str(self.pk)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return self.name

    def get_short_name(self):
        return self.name

    def __str__(self):
        return self.name
