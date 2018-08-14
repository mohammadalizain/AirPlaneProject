from django.shortcuts import render
from .models import airplanes
# Create your views here.

def list_view(request):
    objects = airplanes.objects.all()
    context = {
        "object_list": objects,
    }
    return render(request, 'list_page.html', context)