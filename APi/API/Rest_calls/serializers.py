from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import CricketTeam, CricketPlayer


class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User 
        fields = ['userName', 'email']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CricketPlayer
        field = [  'age', 'handed', 'bowling_type', 'battingVspin' , 'battingVpace' , 'bowling', 'exp', 'fielding' , 'player_region'  ]


class GroupSerializer ( serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
class TeamSerializer ( serializers.ModelSerializer):
    class Meta:
        model = CricketTeam
        #comeplete this function with model and make mirgation and in total 
        fields = [ 'teamName','teamImage','userRegion' ]