from django.db import models
from stdimage.models import StdImageField


class Base(models.Model):
    criado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Cargo(Base):
    cargo = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Cargo'
        verbose_name_plural = 'Cargos'

    def __str__(self) -> str:
        return self.cargo


class Funcionario(Base):
    nome = models.CharField('Nome', max_length=100)
    biografia = models.TextField('Bio', max_length=1000)
    cargo = models.ForeignKey('Cargo', on_delete=models.SET_NULL, null=True)
    foto = StdImageField('Foto',
                         upload_to='equipe',
                         variations={'thumbnail': {'width': 600,
                                                   'height': 600,
                                                   'crop': True}})
    facebook = models.CharField('Face', max_length=100)
    twitter = models.CharField('Twitter', max_length=100)
    instagram = models.CharField('Insta', max_length=100)

    class Meta:
        verbose_name = 'Funcionário'
        verbose_name_plural = 'Funcionários'

    def __str__(self) -> str:
        return self.nome


class Servico(Base):
    image = StdImageField('Imagem',
                          upload_to='servicos',
                          variations={'thumbnail': {'width': 600,
                                                    'height': 600,
                                                    'crop': True}})
    nome = models.CharField('Nome', max_length=100)
    descricao = models.TextField('Descrição', max_length=1000)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self) -> str:
        return self.nome
