from pyclbr import readmodule
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
    #user = UserSerializer.get_fields(many=True)
    #   wuser = serializers.ALL_FIELDS
    class Meta:
        model = models.Disinformation
        fields = '__all__'

class DisinformationGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Disinformation
        fields = ['key']



'''
class AnalisysSerializer(serializers.ModelSerializer):
    class Meta:
        models = models.Analisys
        fields = '__all__'
'''
