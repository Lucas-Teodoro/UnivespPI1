from django.db import models

class TCA(models.Model):

    tcaNum = models.CharField(max_length = 10)
    razaoSocial = models.CharField(max_length = 100)
    endereco = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 40)
    cpfcnpj = models.CharField(max_length = 15)

    def __str__ (self) -> str:
        return self.tcaNum

class AC(models.Model):

    ACNum = models.CharField(max_length = 10)
    area = models.CharField(max_length = 10)
    
    def __str__ (self) -> str:
        return self.ACNum