from django.contrib import admin
from .models import Post, Comentario

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'slug', 'status', 'criado_em')
    list_filter = ('status',)
    search_fields = ('title', 'conteudo')
    prepopulated_fields = {'slug': ('titulo',)}

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'conteudo', 'post', 'criado_em')
    list_filter = ('criado_em',)
    search_fields = ('nome', 'conteudo')
    
admin.site.register(Post, PostAdmin)
admin.site.register(Comentario, ComentarioAdmin)