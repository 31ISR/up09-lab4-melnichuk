from django.shortcuts import render
from .models import Communities

# Create your views here.

def comms_list(req):
    comms = Communities.objects.all().order_by('-date')
    return render(req, 'communities/comms_list.html', {'comms': comms})

def comm_page(req, slug):
    comm = Communities.objects.get(slug=slug)
    return render(req, 'communities/comm_page.html', {'comm': comm})