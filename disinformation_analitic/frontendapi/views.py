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
from post_analitic import machine

class DisinformationViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.DisinformationSerializer
    queryset = models.Disinformation.objects.all()

    

    

    def create(self, request, *args, **kwargs):
        data = request.data #Captura dados do post

        data_text = data['text']#Captura texto do json do post
        data_choice = data['choice']#Captura escolha do metodo de ia do usuário
        result = treatentry(data_text)#Chama classe que analisa o texto e guarda o valor da inferencia

        if(result == True):
            #print(result)

            #teste = machine.machine(data_text, data_choice)#Função que executa a machine learning


            #Processo de armazenamento do disinformation
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)

            #Processo de deserialização dos dados desinformation do banco de dados, objetivo aninhar as informações e capturar o id
            disinformation = models.Disinformation.objects.get(key = data['key'])
            serial = serializers.DisinformationReturnData(disinformation)
            
            return Response(serial.data, status=status.HTTP_201_CREATED, headers=headers)

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

