from rest_framework import serializers
from rest_framework.authtoken.models import Token
from allauth.account.adapter import get_adapter
from django.contrib.auth import get_user_model
from dj_rest_auth.registration.serializers import RegisterSerializer
from .models import User
User = get_user_model()

class CustomDetailSerializer(serializers.ModelSerializer):
   class Meta:
      model = User
      fields = '__all__'
      # exclude = ['password1']  # password 필드 제외


class CustomRegisterSerializer(RegisterSerializer):
    # 추가할 필드들을 정의합니다.
    nickname = serializers.CharField(
    required=False,
    allow_blank=True,
    max_length=30
    )
    gender = serializers.ChoiceField(
        choices=User.GENDER_CHOICES,
        required=False,
        allow_blank=True
    )
    email = serializers.EmailField(required=False)
    phone_number = serializers.CharField(required=False)
    age = serializers.IntegerField(required=False)
    money = serializers.IntegerField(required=False)
    salary = serializers.IntegerField(required=False)
    # financial_products = serializers.ListField(child=serializers.IntegerField(), required=False)


    def get_cleaned_data(self):
      return {
      'username': self.validated_data.get('username', ''),
      'password1': self.validated_data.get('password1', ''),
      'nickname': self.validated_data.get('nickname', ''),
      'age': self.validated_data.get('age', ''),
      'money': self.validated_data.get('money', ''),
      'gender': self.validated_data.get('gender', ''),
      'email': self.validated_data.get('email', ''),
      'phone_number': self.validated_data.get('phone_number', ''),
      'salary': self.validated_data.get('salary', ''),
      # 'financial_products': self.validated_data.get('financial_products', ''),
      }
    
    def save(self, request):
      adapter = get_adapter()
      user = adapter.new_user(request)
      self.cleaned_data = self.get_cleaned_data()
      adapter.save_user(request, user, self)
      self.custom_signup(request, user)
      return user
    

class CustomTokenSerializer(serializers.ModelSerializer):
    username= serializers.SerializerMethodField()
    nickname= serializers.SerializerMethodField()
    email= serializers.SerializerMethodField()

    def get_username(self,obj):
      return obj.user.username
    
    def get_nickname(self,obj):
      return obj.user.nickname

    def get_email(self,obj):
      return obj.user.email

    class Meta:
      model = Token
      fields = ('key', 'user', 'username','nickname','email')

