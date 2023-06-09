from rest_framework.authentication import get_authorization_header, BaseAuthentication
from rest_framework import exceptions
from authentication.models import CustomUser
import jwt
from django.conf import settings


class JWTAuthentication(BaseAuthentication):
    
    def authenticate(self, request):
        auth_header = get_authorization_header(request)
        auth_data = auth_header.decode('utf-8')
        
        auth_token = auth_data.split(" ")
        
        if len(auth_token) != 2 :
            raise exceptions.AuthenticationFailed("Token not valid")
        
        token = auth_token[1]
        
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms='HS256')
            username = payload['username']
            user = CustomUser.objects.get(username=username)
            return (user, token)
        except jwt.ExpiredSignatureError as exc:
            raise exceptions.AuthenticationFailed('Token is expired, login again')
        
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed("Token is invelid!!")
        
        except CustomUser.DoesNotExist:
            raise exceptions.AuthenticationFailed("no Such a client")
        return super().authenticate(request)