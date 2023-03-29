from django.shortcuts import render

from rest_framework import viewsets,views,permissions , generics,response,authentication
from django.contrib.auth import login
from .serializers import UserSerializer, Loginserializer
from .models import Users


from django.views.decorators.csrf import requires_csrf_token, ensure_csrf_cookie, csrf_protect
# Create your views here.
from django.contrib.auth.models import User, Group 
from rest_framework import viewsets 
from rest_framework import permissions
from Rest_calls.serializers import UserSerializer, PlayerSerializer , GroupSerializer, TeamSerializer
from .models import CricketPlayer,CricketTeam
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.contrib.auth.decorators import login_required
from rest_framework.parsers import JSONParser
from rest_framework.decorators import APIView, api_view


import random
class CreatTeam(APIView):
    # queryset = CriketPlayer.objects.all()
    # serializer_class = PlayerSerializer
    # permission_classes = [permissions.IsAdminUser]
    parser_classes = [JSONParser]
    def creatPlayer (self,request, TeamID):
        #         player combination{
        # inclusive 
        #     7 batsmen {
        #         2 with good stars : between 7-10 stars {in both bowling vs spin and pace}
        #         3 with average stars : between 5-7 
        #         2 with below average stars : 3-5
        #         2 wicketkeeper with 6-10 stars in wicketppeking
        #     }
        #     7 bowler {
        #         randomly mixed with 2-3 bowler in each bowling type
        #         2 with good stars : between 7-10 stars {in bowling}
        #         3 with average stars : between 5-7 
        #         2 with below average stars : 3-5
        #     } 
        #     2 allrounders {
        #     random average between 5-9 in batting
        #     random average between 5-9 in bowling
        #     }
        # } 
        F_name = [" john, william"]
        S_name = ['stark', 'river wood ']

        for batsmen in range(1,8):
            name = random.choice(F_name ) + random.choice(S_name)
            if ( batsmen<3):
                SpinVstar= random.randrange(7,10)
                paceVstar= random.randrange(7,10)
            elif ( batsmen< 6):
                SpinVstar= random.randrange(5,7)
                paceVstar= random.randrange(5,7)
            elif ( batsmen< 8):
                SpinVstar= random.randrange(3,5)
                paceVstar= random.randrange(3,5)
            elif batsmen< 10:
                star = random.randrange (3,6)
            bats_bowling = random.randrange
            instance = CricketPlayer(name = name, age = random.randrange(18, 24), handed = random.choice(['left', 'right']) , bowlingtype = random.choice(['fast','medium','off-spin', 'leg-spin']), battingVspin = SpinVstar, battingVpace = paceVstar,bowling = bowlling_stars , experience = random.randrange(3-6) , fielding = random.randrange(4, 8),TeamID = TeamID)
            instance.save()

        for bowler in range(1,8):
            name = random.choice(F_name ) + random.choice(S_name)
            bowler_type = random.choice(['fast','medium','off-spin', 'leg-spin'])
            if ( bowler <3 ):
                stars = random.randrange(7,10)
            elif bowler<6 : 
                stars = random.randrange(5,7)
            else:
                stars = random.randrange(3,5)
            instance = CricketPlayer(name = name, age = random.randrange(18, 24), handed = random.choice(['left', 'right']) , bowlingtype = bowler_type, battingVspin = random.randrange(1,3) , battingVpace = random.randrange(1,3),bowling = stars , experience = random.randrange(3-6) , fielding = random.randrange(4, 8),TeamID = TeamID)
            instance.save()

        for allrounders in range ( 3 ):
            name = random.choice(F_name ) + random.choice(S_name)

            batting_stars = random.randrange(5-9)
            bowlling_stars = random.randrange(5- 9)
            instance = CricketPlayer(name = name, age = random.randrange(18, 24), handed = random.choice(['left', 'right']) , bowlingtype = bowler_type, battingVspin = batting_stars , battingVpace = random.randrange(5,9),bowling = bowlling_stars , experience = random.randrange(3-6) , fielding = random.randrange(4, 8), TeamID = TeamID)
            instance.save()
            
    
    #@ensure_csrf_cookie
    @api_view(['GET', 'POST'])
    def team( request, format = None ):

        if request.method == 'POST' or request.method== 'PUT':
            serializer = TeamSerializer(data=request.data)
            teamName = serializer.data.get("teamName")
            team= CricketTeam.objects.get(name = teamName  )
            if serializer.is_valid():
                serializer.save()
                CricketPlayer(team.id )
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response("better luck next time")
    
    @login_required
    @api_view(['GET'])
    def viewPlayers(request , teamName  ):
        if request.method == 'GET':
            teamMembers  = CricketPlayer.objects.filter(TeamId =CricketTeam.objects.get(teamName = teamName) )
            print("fter this")
            serializer = PlayerSerializer(data =teamMembers, many = True)
          
            
            if not serializer.is_valid():
                print (serializer.errors) 
            print(serializer.data)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("better luck next time")



        
        
class CsrfExemptSessionAuthentication(authentication.SessionAuthentication):
    def enforce_csrf(self, request):
        return

class UserViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all().order_by('name')
    serializer_class = UserSerializer


class LoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)

    def post(self, request):
        print("hgfg")
        serializer = Loginserializer(data=request.data,context={'request': request})  
        print("hgfg")
        serializer.is_valid(raise_exception=True) 
        print("hgfg")
        user = serializer.validated_data['user']
        print("hgfg")
        login(request, user)
        return response.Response(UserSerializer(user).data)