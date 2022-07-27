from rest_framework.authentication import get_authorization_header,BaseAuthentication
from rest_framework import exceptions
from django.contrib.auth.models import User
import jwt

class Authentication(BaseAuthentication):
    def authenticate(self, request):
        auth_header = get_authorization_header(request)

        auth_data = auth_header.decode('utf-8')
        auth_token = auth_data.split(" ")

        if len(auth_token) !=2:
            raise exceptions.AuthenticationFailed("TOKEN NOT VALID")
        
        token = auth_token[1]

        try:
            payload = jwt.decode(token,"secret",algorithms=["HS256"])
            try:
                user = User.objects.get(id=payload['id'])
            except Exception:
                raise exceptions.AuthenticationFailed('user does not exists')
            return (user,token)
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed('token is expired login again')
        
        except jwt.DecodeError:
            raise exceptions.AuthenticationFailed("TOKEN IS INVALID")

        except User.DoesNotExist:
           raise exceptions.AuthenticationFailed("NO SUCH USER") 



