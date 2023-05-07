from django.db import models

class Bairro (models.Model):

    cep = models.CharField(max_length = 8)
    abairramento2018 = models.CharField(max_length = 100)

    def __str__ (self) -> str:
        return self.cep
    
#class Cartorio (models.Model):

#    cartorio = models.CharField(max_length = 100)

#    def __str__ (self) -> str:
#        return self.cep
    
class Solicitante (models.Model):

    razaoSocial = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 40)
    cpfcnpj = models.CharField(max_length = 15)

    def __str__ (self) -> str:
        return self.cpfcnpj
    
class Imovel (models.Model):

    imImovel = models.CharField(max_length = 11)
    endereco = models.CharField(max_length = 100)
    quadra = models.IntegerField()
    lote = models.IntegerField()
    complemento = models.CharField(max_length = 100)
    arealote = models.FloatField(max_length = 11)
    areaSupressao = models.FloatField(max_length = 11)
    areaConstruida = models.FloatField(max_length = 11)
    areaPreservacao = models.FloatField(max_length = 11)
    averbacaoMatricula = models.CharField(max_length = 30)

    def __str__ (self) -> str:
        return self.imImovel

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