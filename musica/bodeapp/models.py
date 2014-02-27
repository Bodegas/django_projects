from django.db import models

# Create your models here.
class Musico(models.Model):
    nome = models.CharField(max_length=255, blank=True, verbose_name=u'nome')
    apelido = models.CharField(max_length=255, blank=True, verbose_name=u'apelido')
    instrumento = models.CharField(max_length=255, blank=True, verbose_name=u'instrumento')
    idade = models.IntegerField(verbose_name=u'idade')

    def __unicode__(self):
        return self.nome
    
    class Meta:
        verbose_name = u'Musico'
        verbose_name_plural = u'Musicos'

class Disco(models.Model):
    titulo = models.CharField(max_length=255, blank=True, verbose_name=u'titulo')
    ano = models.DateField(null=True, verbose_name=u'ano')
    xenero = models.CharField(max_length=255, blank=True, verbose_name=u'xenero')
    musicos = models.ManyToManyField(u'Musico')

    def __unicode__(self):
        return self.titulo

class Discografica(models.Model):
    nome = models.CharField(max_length=255, blank=True, verbose_name=u'nome')
    discos = models.ManyToManyField(u'Disco')

    def __unicode__(self):
        return self.nome


