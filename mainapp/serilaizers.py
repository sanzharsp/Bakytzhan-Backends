from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.core.exceptions import ObjectDoesNotExist




class RegistrationSerializer(serializers.ModelSerializer):
    """ Сериализация регистрации пользователя и создания нового. """

    # Убедитесь, что пароль содержит не менее 8 символов, не более 128,
    # и так же что он не может быть прочитан клиентской стороной


    password = serializers.CharField(
        max_length=128,
        min_length=4,
        write_only=True,
        label="Пароль"

    )

    # Клиентская сторона не должна иметь возможность отправлять токен вместе с
    # запросом на регистрацию. Сделаем его доступным только на чтение.


    class Meta:
        model = User
        # Перечислить все поля, которые могут быть включеWны в запрос
        # или ответ, включая поля, явно указанные выше.
        fields = [
        'email',
        'password',
        ]

        


class LogoutSerilizers(serializers.Serializer):
    refresh_token = serializers.CharField(
        write_only=True,
        label="Refresh токен"

    )




class UserSerilizer(serializers.ModelSerializer):
    date_create = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    class Meta:
        model = User
        fields = 'email', 'date_create'

class AuthorizateSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        refresh = self.get_token(user)
        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['user'] =UserSerilizer(User.objects.get(email=user)).data
        return data

class LogoSerilezer(serializers.ModelSerializer):
    logo = serializers.ImageField()
    class Meta:
        model = Logo
        fields = 'logo', 
    

class ParkingSerilezer(serializers.ModelSerializer):

    class Meta:
        model = Parking
        fields = '__all__', 
    







