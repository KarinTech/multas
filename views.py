from django.shortcuts import render, get_object_or_404, redirect
from .models import Multa
from .forms import MultaForm

def lista_multas(request):
    multas = Multa.objects.all()
    return render(request, 'multas/lista_multas.html', {'multas': multas})

def detalle_multa(request, multa_id):
    multa = get_object_or_404(Multa, id=multa_id)
    return render(request, 'multas/detalle_multa.html', {'multa': multa})

def crear_multa(request):
    if request.method == 'POST':
        form = MultaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_multas')
    else:
        form = MultaForm()
    return render(request, 'multas/crear')
