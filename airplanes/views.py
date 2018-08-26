from django.shortcuts import render, redirect
from .models import airplanes
from .forms import airplanesForm, UserLogin, UserRegister
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
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

@login_required
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



def user_login(request):
    form = UserLogin()
    if request.method == 'POST':
        form = UserLogin(request.POST)
        if form.is_valid():
            print('username')

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                print('login')
                login(request, auth_user)
                # Where you want to go after a successful login
                return redirect('list-page')

    context = {
        "form":form
    }
    return render(request, 'login.html', context)


 
def user_register(request):
    form = UserRegister()
    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            # Where you want to go after a successful signup
            return redirect("list-page")
    context = {
        "form":form,
    }
    return render(request, 'registration.html', context)

def user_logout(request):
    logout(request)
    # Where you would like to redirect the user after successfully logging out
    return redirect("login-page")



def some_view(request):
    if request.user.is_anonymous:
        return print('not Authurized')