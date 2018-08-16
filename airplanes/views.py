from django.shortcuts import render, redirect
from .models import airplanes
from .forms import airplanesForm

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


def create_view(request):
    form = airplanesForm()
    if request.method == "POST":
        form = airplanesForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list-page')
    context = {
    "form":form
    }
    return render(request, 'create_page.html', context)

def update_view(request, obj_id):
    obj = airplanes.objects.get(id=obj_id)
    form = airplanesForm(instance=obj)
    if request.method == "POST":
        form = airplanesForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("list-page")
    context = {
        "obj":obj,
        "form":form
    }
    return render(request, 'update_page.html', context)


def delete_view(request, object_id):
    airplanes.objects.get(id=object_id).delete()
    return redirect("list-page")