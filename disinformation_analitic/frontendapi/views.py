import email
from venv import create
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, action
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from . import serializers
from . import models
from post_inference.analitic import treatentry

class DisinformationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DisinformationSerializer
    queryset = models.Disinformation.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data 

        #Neste momento entra o objeto que irá fazer a inferencia dos dados e análise(Os dois termos serão executados na mesma classe?) post_inference e post_analitic

        data_text = data['text']
        result = treatentry(data_text)

        if(result == True):



            print(result)
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
        
            return Response("Api conectada com sucesso", status=status.HTTP_201_CREATED, headers=headers)

        else:

            return Response("Seu texto não corresponde aos padrões para a análise", status=status.HTTP_400_BAD_REQUEST)

class DisinformationGetViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DisinformationGetSerializer
    queryset = models.Disinformation.objects.all()

    def create(self, request, *args, **kwargs):

        data = request.data 
        key = data['key']

        try:

            disinformation = models.Disinformation.objects.get(key = key)

            serializer = serializers.DisinformationSerializer(disinformation)
            return Response(serializer.data, status=status.HTTP_302_FOUND)

        except:
             return Response("Disinformation don't exist", status=status.HTTP_404_NOT_FOUND)

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserSerializer
    queryset = models.User.objects.all()

class UserVerificationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserVerificationSerializer
    queryset = models.User.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data 
        email = data['email']
        password = data['password']

        try:
            user = models.User.objects.get(email= email)
            print(user.name)

            if(password == user.password):
                serializer = serializers.UserSerializer(user)
                return Response(serializer.data, status=status.HTTP_302_FOUND)
            else:
                return Response("wrong password", status=status.HTTP_201_CREATED)

        except:
             return Response("User don't exist", status=status.HTTP_404_NOT_FOUND)
        
class UserGetDisinformationsViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UserGetDisinformationsSerializer
    queryset = models.Disinformation.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data 
        user = data['user']
        
        try:

            disinformations = models.Disinformation.objects.filter(user = user)

            serializer = serializers.DisinformationSerializer(disinformations, many=True)

            return Response(serializer.data, status=status.HTTP_302_FOUND)

        except:

             return Response("User don't exist", status=status.HTTP_404_NOT_FOUND)
       
    

'''

--@verifato jdkbcWLJBVWHBVHBVWHABVHWBVHWBWHB -- Função(Classe)
-- jdkbcWLJBVWHBVHBVWHABVHWBVHWBWHB  -- Função que elimina o @
-- Conta os caratcteres -- 500 ^ 2500 --
-- Filtro qualquer caracter -- 

-- Machine Learning --




-- Linguagem -- Inglês ou não -- 



#Mais uma api seria essencial para coletar os dados do usuário junto com as analises feitas
'''

