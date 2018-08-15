from django.shortcuts import render
from .models import airplanes
# Create your views here.

def list_view(request):
    objects = airplanes.objects.all()
    context = {
        "object_list": objects,
    }
    return render(request, 'list_page.html', context)


def detail_view(request, id):
    context = {
        "detail": airplanes.objects.get(pk=id)
        
    }
    return render(request, 'detail_page.html', context)