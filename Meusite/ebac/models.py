from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = (
    (0, 'Rascunho'),
    (1, 'Publicado')
)

class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    editado_em = models.DateTimeField(auto_now=True)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ['-criado_em']
        
    def __str__(self):
        return self.titulo
    
class Comentario(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comentarios')
    nome = models.CharField(max_length=80)
    conteudo = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['criado_em']
    
    def __str__(self):
        return 'comentario {} por {}'.format(self.conteudo, self.nome)