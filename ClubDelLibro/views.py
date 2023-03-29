from django.shortcuts import render
from ClubDelLibro.models import Biblioteca, Profile, Mensaje
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def index(request):
    return render(request, "ClubDelLibro/index.html")


class BibliotecaList(ListView):
    model = Biblioteca  
    context_object_name = "Bibliotecas"

class BibliotecaMineList(LoginRequiredMixin, BibliotecaList):

    def get_queryset(self):
        return Biblioteca.objects.filter(propietario=self.request.user.id).all()



class PermisoBibliotecario(UserPassesTestMixin):
    def test_func(self):
        user_id = self.request.user.id
        biblioteca_id =  self.kwargs.get("pk")  
        return Biblioteca.objects.filter(book=user_id, id=biblioteca_id).exists()




class BibliotecaUpdate(LoginRequiredMixin, PermisoBibliotecario, UpdateView):
    model = Biblioteca
    success_url = reverse_lazy("biblioteca-list")
    fields = '__all__'


    

class BibliotecaDelete(LoginRequiredMixin, PermisoBibliotecario, DeleteView):
    model = Biblioteca
    context_object_name = "Biblioteca"
    success_url = reverse_lazy("biblioteca-list")

    


class BibliotecaCreate(LoginRequiredMixin, CreateView):
    model = Biblioteca
    success_url = reverse_lazy("biblioteca-create")
    fields = '__all__'


class BibliotecaSearch(ListView):
    model = Biblioteca
    context_object_name = " Bibliotecas"

    def get_queryset(self):
        criterio = self.request.GET.get("criterio")
        result = Biblioteca.objects.filter(carousel_caption_title__icontains=criterio).all()
        return result

class Login(LoginView):
    next_page = reverse_lazy("biblioteca-list")
    


class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('biblioteca-list')
    

class Logout(LogoutView):
    template_name = "registration/logout.html"


def Historia(request):
    return render(request, "ClubDelLibro/biblioteca_historia.html")  


class ProfileCreate(CreateView):
    model = Profile
    success_url = reverse_lazy("biblioteca-list")
    fields = ["avatar"]

    def form_valid(self,form):
        form.instance.user = self.request.user 
        return super().form_valid(form)
    

class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = Profile
    success_url = reverse_lazy("biblioteca-list")
    fields = ['avatar',] 

    def test_func(self):
        return Profile.objects.filter(user=self.request.user).exists()    
    


class MensajeCreate(CreateView):
    model = Mensaje
    success_url = reverse_lazy('mensaje-create')
    fields = '__all__'  


class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensaje
    context_object_name = "mensaje"
    success_url = reverse_lazy("mensaje-list")

    def test_func(self):
        return Mensaje.objects.filter(destinatario=self.request.user).exists()
    

class MensajeList(LoginRequiredMixin, ListView):
    model = Mensaje
    context_object_name = "mensajes"

    def get_queryset(self):
        import pdb; pdb.set_trace
        return Mensaje.objects.filter(destinatario=self.request.user).all()
    



def SinDetalles(request):
    return render(request, "ClubDelLibro/sin_detalles.html")     


    





         
        





