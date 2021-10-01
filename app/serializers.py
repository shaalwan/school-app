from rest_framework import serializers
from .models import *
from django.db.models import fields
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
  username = serializers.CharField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
  password = serializers.CharField(min_length=8, write_only=True)
  registeration_id = serializers.CharField(max_length=100)
  class Meta:
    model = User
    fields = ['username','password','name','standard','roll_number','father_name','registeration_id']

class addUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['username','password','name','standard','roll_number','father_name','pk']