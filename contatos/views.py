from django.core.paginator import Paginator
from django.db.models import Q, Value
from django.db.models.functions import Concat
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Contato


def index(request):
    
    contatos = Contato.objects.order_by("-id").filter(
        mostrar=True
    )
    
    paginator = Paginator(contatos, 2) # Show 25 contacts per page.
    
    page = request.GET.get('p')
    
    contatos = paginator.get_page(page)
    
    context = {
        "contatos":contatos,
    }
    
    return render(request,'contatos/index.html',context)

def vercontato(request,pk):
    
    contato = get_object_or_404(Contato,id=pk)

    if not contato.mostrar :
        raise Http404()
    
    context = {
        "contato":contato,
    }
    
    return render(request,'contatos/ver_contato.html',context)


def busca(request):
    
    campos = Concat('nome',Value(' '), 'sobrenome')
    
    termo  = request.GET.get('termo')
    
    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(telefone__icontains=termo)
    )
    
    if termo is None:
        raise Http404()
    
    paginator = Paginator(contatos, 2) # Show 25 contacts per page.
    
    page = request.GET.get('p')
    
    contatos = paginator.get_page(page)
    
    context = {
        "contatos":contatos,
    }
    
    return render(request,'contatos/busca.html',context)


