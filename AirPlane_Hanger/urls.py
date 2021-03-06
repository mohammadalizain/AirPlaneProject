"""AirPlane_Hanger URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import  path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from airplanes.views import list_view, detail_view, create_view, update_view, delete_view, user_login, user_register, user_logout
from api.views import ListView, Detailview , CreateView, UpdateView, DeleteView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', list_view, name="list-page"),
    path('detail/<int:id>', detail_view, name="detail-page"),
    path('create/', create_view, name='create-page'),
    path('update/<int:obj_id>', update_view, name='update-page'),
    path('delete/<int:object_id>', delete_view, name='delete-page'),
    path('List/<int:object_id>', ListView.as_view(), name='List-page'),
    path('details/view/<int:object_id>', Detailview.as_view(), name='Detailview-page'),
    path('create/view/<int:object_id>', CreateView.as_view(), name='CreateView-page'),
    path('update/view/<int:object_id>', UpdateView.as_view(), name='UpdateView-page'),
    path('delete/view/<int:object_id>', DeleteView.as_view(), name='DeleteView-page'),
    path('login/view/', user_login, name='login-page'),
    path('registration/view/', user_register, name='register-page'),
    path('logout/', user_logout, name='logout-page'),
]




urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)