from django.shortcuts import render
from django.http import HttpResponse

from pilots.models import Pilots

# Create your views here.
def create_pilot(request):
    new_pilot = Pilots.objects.create(name='Di Palma', points=85, enabled=True)
    print(new_pilot)
    return HttpResponse('nuevo piloto')

def list_pilots(request):
    all_pilots = Pilots.objects.all()
    print(all_pilots)
    context = {
        'pilots':all_pilots,
    }
    return render(request, 'list_pilots.html' , context=context)


