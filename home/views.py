from django.shortcuts import render
from home.models import *


def HomeView(request):
    """
    Home page view
    """
    
    all_jewelry = Jewelry.objects.filter(sold=False).order_by('type')
    rings = Jewelry.objects.filter(sold=False, type='anillo').order_by('price_int')
    earrings = Jewelry.objects.filter(sold=False, type='aros').order_by('price_int')
    pendants = Jewelry.objects.filter(sold=False, type='colgante').order_by('price_int')
    bracelets = Jewelry.objects.filter(sold=False, type='pulsera').order_by('price_int')
    necklaces = Jewelry.objects.filter(sold=False, type='collar').order_by('price_int')
    sets = Jewelry.objects.filter(sold=False, type='conjunto').order_by('price_int')

    context = {
        'all_jewelry': all_jewelry,
        'rings': rings,
        'earrings': earrings,
        'pendants': pendants,
        'bracelets': bracelets,
        'necklaces': necklaces,
        'sets': sets,
    }

    return render(request, 'home.html', context)
