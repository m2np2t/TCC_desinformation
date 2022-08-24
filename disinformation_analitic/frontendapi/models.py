from django.db import models

# Create your models here.

#O ideal aqui seria criar uma classe somente para a analise e associa-la como chave estrangeira a desinformação
#Usuários terão que se cadastrar para analise(Entendimento nescessários para associação)


class Disinformation(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    text = models.CharField(max_length=255)
    type_analysis = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return (self.titulo)

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return (self.name)

class Analisy(models.Model):
    classification = models.CharField(max_length=255)
    porcentage = models.FloatField
    him = models.CharField(max_length=255)
    time = models.TimeField

    def __str__(self):
        return (self.classification)






    #analisys
    #Identificador

#Pré definição da classe da analise 
'''
class Analisys(models.Model):
    Classificacao = models.CharField(max_length=255)
    porcentagem = models.FloatField 
    Tema =  models.ExpressionList
    Tempo = models.FloatField
'''






    
