from django.contrib.auth.models import User
from rest_framework import serializers
from studApp.models import StdModel

from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","email","password"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=StdModel
        fields="__all__"
        read_only_fields=['id','name']


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email']

