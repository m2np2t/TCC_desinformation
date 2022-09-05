from django.db import models
#O ideal aqui seria criar uma classe somente para a analise e associa-la como chave estrangeira a desinformação
#Usuários terão que se cadastrar para analise(Entendimento nescessários para associação)


class Disinformation(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=255)
    link = models.CharField(max_length=255, null=True)
    text = models.CharField(max_length=255)
    title = models.CharField(max_length=255, null=True)
    choice = models.CharField(max_length=255, null=True)
    user = models.ForeignKey("User", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return (self.titulo)

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        #return (self.name)
        return f"{self.name}, {self.email}"

class Analisy(models.Model):
    classification = models.FloatField
    time = models.TimeField(null=True)
    disinformation = models.ForeignKey("Disinformation", on_delete=models.CASCADE, null=False)
    #top5 = 

    def __str__(self):
        return (self.classification)

class themes(models.Model):
    origin = models.FloatField(null=True)
    statistic = models.FloatField(null=True)
    economic = models.FloatField(null=True)
    discredit = models.FloatField(null=True)
    symptons = models.FloatField(null=True)
    society = models.FloatField(null=True)
    politicization = models.FloatField(null=True)
    celebrity = models.FloatField(null=True)
    analisy = models.ForeignKey("Analisy", on_delete=models.CASCADE, null=False)
'''
class top5(models.Model):
    first = models.CharField(max_lenght=255)
    second = models.CharField(max_lenght=255)
    third = models.CharField(max_lenght=255)
    fourth = models.CharField(max_lenght=255)
    fifth = models.CharField(max_lenght=255)
    analisy = models.ForeignKey("Analisy", on_delete=models.CASCADE, null=False)








    #analisys
    #Identificador

#Pré definição da classe da analise 
'''







    
