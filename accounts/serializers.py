from rest_framework import serializers
from .models import User

class UserSignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {
            'password': {'write_only': True},  # write_only: 필드를 작성할 때만 사용,응답에서 제외
            'email': {'required': True},  # required': True : 필드 필수! 요청시 반드시 제공해어야한다
            'username': {'required': True},   
            'first_name': {'required': True},  
            'nickname': {'required': True}, 
            'birthday': {'required': True}  
        }

class LoginSerializer(serializers.Serializer): #ModelSerializer(데이터베이스연동하여 인스턴스생성,업데이트에 사용)
    username=serializers.CharField()            #Serializer > 단순히 클라이언트가 제공한 데이터를 검증,인증에 사용
    password=serializers.CharField()    