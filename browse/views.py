from django.shortcuts import render
from django.http import HttpResponse
import json

context = {
    'navbarData': [],
}

navbarItems = (
    # (Menu Item Name, Item URL)
    ('Home', '/'),
    ('Contact', '/contact'),
)

for i in navbarItems:
    context['navbarData'].append({
        'name': i[0],
        'url': i[1]
    })

def index(request):
    return render(request, 'browse/index.html', context=context)

def contact(request):
    return render(request, 'browse/contact.html', context=context)
