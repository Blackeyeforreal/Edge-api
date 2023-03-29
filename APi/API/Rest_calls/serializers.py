from django.contrib.auth.models import User,Group
from rest_framework import serializers
from .models import CricketTeam, CricketPlayer



from rest_framework import serializers, status
from rest_framework.response import Response
from .models import Users

from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ('email','name', 'password',


                                  'id',
                  'last_login',

                  'is_active',
                  'joined_at',

                  )
        read_only_fields = ('last_login', 'is_active', 'joined_at')


    #def create(self, validated_data):

        #k = validated_data['name']
        #if Users.objects.filter(name =  k).exists():
            #raise Exception
         #   print('yeash we get herer')
          #  return Response( {'name': 'Name already exists' }  , status=status.HTTP_208_ALREADY_REPORTED)
        #else:
     #       return  Users.objects.create(**validated_data)

    def validate(self, data):
        data = super(UserSerializer, self).validate(data)
        k = data['name']

        if Users.objects.filter(name = k).exists():
            raise serializers.ValidationError("User already exists")
        return data

    def create(self, validated_data):
        return Users.objects.create_user(
            validated_data.pop('email'),
            validated_data.pop('password'),
            **validated_data
        )

class Loginserializer(serializers.Serializer):
    email= serializers.EmailField()
    password = serializers.CharField()


    def validate(self, attrs):
        print(Users.objects.get(email = attrs["email"]))
        k =Users.objects.get(email = attrs["email"])
        if k and  k.password == (attrs["password"]): 
            
            user = k
        print(attrs['password'], Users.objects.get(name="bro"))
        if not user:
            raise serializers.ValidationError('Incorr6ect email or password.')

        if not user.is_active:
            raise serializers.ValidationError('User is disabled.')

        return {'user': user}


# class UserSerializer(serializers.ModelSerializer):
#     class Meta: 
#         model = User 
#         fields = ['userName', 'email']

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CricketPlayer
        fields = [ 'Name', 'age', 'handed', 'bowlingtype', 'battingVspin' , 'battingVpace' , 'bowling', 'experience', 'fielding' , 'region'  ]


class GroupSerializer ( serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
class TeamSerializer ( serializers.ModelSerializer):
    class Meta:
        model = CricketTeam
        #comeplete this function with model and make mirgation and in total 
        fields = [ 'teamName','teamImage','userRegion' ]