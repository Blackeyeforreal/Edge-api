from django.db import models

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