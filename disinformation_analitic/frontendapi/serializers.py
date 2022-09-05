from ast import Return
from http.client import responses
from pyclbr import readmodule
from pyexpat import model
from urllib import response
from attr import fields
from django.forms import CharField
from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = '__all__'

class UserVerificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ['email', 'password']

class UserGetDisinformationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Disinformation
        fields = ['user']

class DisinformationSerializer(serializers.ModelSerializer):
    #user = UserSerializer(Return)
    #   wuser = serializers.ALL_FIELDS
    class Meta:
        model = models.Disinformation
        fields = '__all__'

class DisinformationReturnData(serializers.ModelSerializer):
    class Meta:
        model = models.Disinformation
        fields = '__all__'
        depth = 1

class DisinformationGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Disinformation
        fields = ['key']

class AnalisySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Analisy
        fields = '__all__'



'''
class AnalisysSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Analisys
        fields = '__all__'
'''
