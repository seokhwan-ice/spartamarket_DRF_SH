from rest_framework import serializers
from .models import User

class UserSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {                        # extra_kwargs. Meta 클래스 추가적인 설정가능
            'password': {'write_only': True},  # write_only: 필드를 작성할 때만 사용,응답에서 제외
            'email': {'required': True},  # required': True : 필드 필수! 요청시 반드시 제공해어야한다
            'username': {'required': True},   
            'first_name': {'required': True},
            'last_name':{'required':True}, 
            'nickname': {'required': True}, 
            'birthday': {'required': True}  
        }
    
    def create(self, validated_data):
        user=super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
        