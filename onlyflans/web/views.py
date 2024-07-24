from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Flan, ContactForm
from .forms import ContactFormModelForm
from django.contrib.auth.decorators import login_required



def indice(request):
    flanes_publicos = Flan.objects.filter(is_private=False).order_by('-id')[:3]
    return render(request, 'index.html', {'flanes': flanes_publicos})

def acerca(request):
    return render(request, 'about.html', {})

def producto(request):
    public_flans = Flan.objects.filter(is_private=False)

    return render(
        request,
        'producto.html', {
            'public_flans': public_flans
        })

@login_required
def user(request):
    private_flans = Flan.objects.filter(is_private=True)

    return render(
        request,
        'user.html', {
            'private_flans': private_flans
        })

def carrito(request):
    return render(request, 'carrito.html', {})

def contacto(request):
    if request.method == 'POST':
        form = ContactFormModelForm(request.POST)
        if form.is_valid():
            contact_form = ContactForm.objects.create(**form.cleaned_data)
            return HttpResponseRedirect('/exito')
    
    else:
        form = ContactFormModelForm()   

    return render(request, 'contactus.html', {'form': form})

def exito(request):
    return render(request, 'success.html', {})

def compra(request):
    return render(request, 'comprar.html', {})

def reembolso(request):
    return render (request, 'reembolso.html', {})

def faq(request):
    return render (request, 'faq.html', {})

