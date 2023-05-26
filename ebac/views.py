from django.shortcuts import render, HttpResponseRedirect
from .models import Post
from .forms import ComentarioForm

# Create your views here.

def home(request):
    post = Post.objects.filter()
    
    conteudo = {
        'post': post
    }
    
    return render(request, 'home.html', conteudo )

def post(request, id):
    template_nome = 'post.html'
    post = Post.objects.get(id=id)
    comentarios = post.comentarios.filter().order_by('-criado_em')
    novo_comentario = None
    
    if request.method == 'POST':
        comentario_form = ComentarioForm(data=request.POST)
        if comentario_form.is_valid():
            novo_comentario = comentario_form.save(commit=False)
            novo_comentario.post = post
            novo_comentario.save()
            return HttpResponseRedirect(request.path_info)
    else:
        comentario_form = ComentarioForm()
        
    return render (
        request,
        template_nome,
        {
            'post': post,
            'comentarios': comentarios,
            'novo_comentario': novo_comentario,
            'comentario_form': comentario_form,
        },
    )