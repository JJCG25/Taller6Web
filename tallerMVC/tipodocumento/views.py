from django.shortcuts import render, HttpResponseRedirect,get_object_or_404
from django.urls import reverse
from django.http import HttpResponse
from django.template import loader
from .models import td
from .forms import tdForm

# Create your views here.


def tiposd(request):
    tipos = td.objects.all()
    template =  loader.get_template('td/tiposd.html')
    context = {'tipos':tipos,}
    return HttpResponse(template.render(context, request))

def create_tiposd(request):
    if request.method == 'POST':

        form = tdForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['nombre']
            description = form.cleaned_data['descripcion']
            td1 = td(nombre = name,descripcion = description)
            td1.save()
            return HttpResponseRedirect(reverse('tiposd'))
    else :
        form = tdForm()
        
    return render(request,'td/create_tiposd.html',{'form':form})
        
def edit_tiposd(request,pk):
    tipodocumento = get_object_or_404(td, pk=pk)
    if request.method == 'POST':

        form = tdForm(request.POST, instance=tipodocumento)

        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tiposd'))
    else:
        form = tdForm(instance=tipodocumento)

    return render(request, 'td/create_tiposd.html', {'form': form})

def delete_tiposd(request, pk):
    tipodocumento = get_object_or_404(td, pk=pk)
    if request.method == 'POST':
        tipodocumento.delete()
        return HttpResponseRedirect(reverse('tiposd'))
    return render(request, 'td/delete_tiposd.html', {'tipodocumento': tipodocumento})
