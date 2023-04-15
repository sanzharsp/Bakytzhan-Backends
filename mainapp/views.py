from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serilaizers import *
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
import jwt as JWT_
from diplom.settings import SIMPLE_JWT
# Create your views here.
#########################################



# Refresh TokenObtainPairView (add user)
class AuthorizateView(TokenObtainPairView):
    serializer_class = AuthorizateSerializer


class IsAuthView(generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    def post(self,request):
        refresh_token_get = request.META.get('HTTP_AUTHORIZATION', ' ').split(' ')[1]
        jwt=JWT_.decode(
            refresh_token_get,
            SIMPLE_JWT['SIGNING_KEY'],
        algorithms = [SIMPLE_JWT['ALGORITHM']],
            )
        
        queryset=User.objects.get(id=jwt['user_id'])
        serilaizers= UserSerilizer(queryset)
        return Response({'user':serilaizers.data}, status=status.HTTP_200_OK)
    

class LogoView(generics.GenericAPIView):
    serializer_class = LogoSerilezer
    
    def get(self, request, *args, **kwargs):
        queryset=Logo.objects.filter().first()
        serilaizers= LogoSerilezer(queryset)
        return Response(serilaizers.data, status=status.HTTP_200_OK)


class PatkingView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ParkingSerilezer
    def post(self, request):

        electron = Parking.objects.filter(id_Parking = request.data['id_Parking'])
        if electron.exists():
            data = electron.first()
            data.number = request.data['number']
            
            data.save()
            return Response(ParkingSerilezer(data).data,status=status.HTTP_200_OK)
        else:
            data = Parking.objects.create(id_Parking = request.data['id_Parking'],number = request.data['number'],  )
            
            return Response(ParkingSerilezer(data).data,status=status.HTTP_200_OK)