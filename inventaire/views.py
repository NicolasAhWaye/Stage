from django.shortcuts import render
from django.http import HttpResponse
from .models import Expiration, GTIN
from django.template import loader
from .form import ContactForm


# Create your views here.

def index(request):
    gtins = GTIN.objects.all().order_by('date_expiration')
    context = {
        'gtins': gtins
    }
    return render(request, 'inventaire/index.html', context)


def couverture(request):
    return render(request, 'inventaire/couverture.html')


def table(request):
    gtins = GTIN.objects.all().order_by('date_expiration')
    context = {
        'gtins': gtins
    }
    return render(request, 'inventaire/table.html', context)


def ajouter(request):
    gtins = GTIN.objects.all().order_by('date_expiration')
    context = {
        'gtins': gtins
    }
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            gtin = form.cleaned_data['gtin']
            date = form.cleaned_data['date']

            produit = GTIN.objects.filter(gtin=gtin)
            if not produit.exists():
                                        gtin = GTIN.objects.create(
                                        gtin=gtin,
                                        date=date
                                        )
            else:
                                        produit.date_expiration = date

            return render(request, 'inventaire/Validation.html', context)
        else:
                context['errors'] = form.errors.items()
    else:
                                    form = ContactForm()
    context['form'] = form

    return render(request, 'inventaire/ajouter.html', context)
