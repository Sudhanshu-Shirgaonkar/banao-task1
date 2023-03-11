from django.shortcuts import render,redirect
from django.views import generic
from .forms import MyUserCreationForm
from django.urls import reverse_lazy,reverse
from django.contrib import messages
from .models import User
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
# Create your views here.


class IndexView(LoginRequiredMixin,generic.TemplateView):

    template_name = 'base/index.html'


class LoginView(LoginView):

    template_name = 'base/login.html'
    

    def get_success_url(self):

        return reverse_lazy('index')
    
    def dispatch(self, request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)
    
  

class RegisterView(generic.TemplateView):

    template_name = 'base/register.html'

    def dispatch(self, request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)






class DoctorRegisterView(SuccessMessageMixin,generic.CreateView):
    model = User
    template_name = 'base/register_patient_doctor.html'
    form_class =  MyUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def form_valid(self, form):

        user = form.save(commit= False)
        user.user_type =2
        user.save()

        return super(DoctorRegisterView, self).form_valid(form)
    

    def dispatch(self, request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)
    


    



class PatientRegisterView(generic.CreateView):
    model = User
    template_name = 'base/register_patient_doctor.html'
    form_class =  MyUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['page'] = "Patient"

        return context
    
    def dispatch(self, request,*args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)
    


class ProfileView(generic.DetailView):

    template_name = 'base/profile.html'
    model = User
    context_object_name = 'context' 

    


class EditProfileView(generic.UpdateView):

    template_name = 'base/edit-profile.html'
    model = User
    fields = ['first_name','last_name','profile_picture','username','email','address']


    def get_success_url(self):
        return reverse("profile", args=[self.object.pk])

    





