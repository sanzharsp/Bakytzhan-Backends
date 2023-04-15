from django.urls import path
from .views import *
from rest_framework_simplejwt.views import (TokenRefreshView,TokenVerifyView,)

urlpatterns = [


    path('api/v1/login', AuthorizateView.as_view()),
    path('api/v1/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('api/v1/check/auth/', IsAuthView.as_view(), name='token_verify'),
    path('api/v1/logo/get', LogoView.as_view(), name='logo'),
    path('api/v1/post/parking', PatkingView.as_view(), name='parking'),


    

]
