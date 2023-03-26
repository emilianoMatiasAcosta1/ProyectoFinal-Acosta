"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ClubDelLibro.views import (index, BibliotecaList, BibliotecaMineList, BibliotecaUpdate, 
                                       BibliotecaDelete, BibliotecaCreate,  Login, Logout, SignUp, Historia)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("biblioteca/list", BibliotecaList.as_view(), name="biblioteca-list"),
    path ("biblioteca/list", BibliotecaMineList.as_view(), name="biblioteca-mine"),
    path ("biblioteca/<pk>/update", BibliotecaUpdate.as_view(), name="biblioteca-update"),
    path ("biblioteca/<pk>/delete", BibliotecaDelete.as_view(), name="biblioteca-delete"),
    path ("biblioteca/create", BibliotecaCreate.as_view(), name="biblioteca-create"),
    path("login/", Login.as_view(), name="login"),
    path("logout/", Logout.as_view(), name="logout"),
    path("signup/", SignUp.as_view(), name="signup"),
    path("biblioteca/historia", Historia, name="biblioteca-historia"),

]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
