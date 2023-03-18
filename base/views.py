from django.shortcuts import render,redirect
from django.views import generic,View
from .forms import MyUserCreationForm,PostForm,AppointmentForm
from django.urls import reverse_lazy,reverse
from .models import User,Post,Appointment
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
import datetime
from googleapiclient.discovery import build
import pickle


# Create your views here.

credentials = pickle.load(open("base/token.pkl", "rb"))
service = build("calendar", "v3", credentials=credentials)



class IndexView(LoginRequiredMixin,generic.ListView):

    template_name = 'base/index.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):
        q = self.request.GET.get('q', None)

        context = Post.objects.filter(
            Q(category = q) &
            Q(is_draft = False)
            ) if q  else Post.objects.filter(is_draft = False)
       

        return context

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['category'] = ['Mental Health','Heart Disease','Covid 19','Immunization']

        return context
    



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
    


class ProfileView(LoginRequiredMixin,generic.DetailView):

    template_name = 'base/profile.html'
    model = User
    context_object_name = 'context' 



    


class EditProfileView(LoginRequiredMixin,SuccessMessageMixin,generic.UpdateView):

    template_name = 'base/edit-profile.html'
    model = User
    fields = ['first_name','last_name','profile_picture','username','email','address']
    success_message = 'Profile Picture Updated'


    def get_success_url(self):
        return reverse("profile", args=[self.object.pk])
    

    def dispatch(self, request,*args, **kwargs):
        pk=self.kwargs['pk']
        if request.user.id != int(pk):
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)
    


    




class CreatePostView(LoginRequiredMixin,SuccessMessageMixin,generic.CreateView):
    template_name = 'base/create-blog.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('index')
    success_message = 'Blog Successfully Posted'

    def form_valid(self, form):
        self.object = form.save(commit=False)

        self.object.created_by = self.request.user
        if 'draft' in self.request.POST:
            self.object.is_draft = True
            self.success_message = 'Blog saved as Draft'
        
            
        self.object.save()

        return super().form_valid(form)
    

    def dispatch(self, request,*args, **kwargs):
        if request.user.user_type == 1:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)

    

class BlogDetailView(LoginRequiredMixin,generic.DetailView):

    template_name = 'base/blog_detail.html'
    model = Post
    context_object_name = 'post'

   
        

class DraftView(LoginRequiredMixin,generic.ListView):

    template_name = 'base/draft.html'

    model = Post
    context_object_name = 'posts'

    def get_queryset(self):

        return Post.objects.filter(Q(created_by=self.request.user) & Q(is_draft =True))
    

    def dispatch(self, request,*args, **kwargs):
        if request.user.user_type == 1:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)
    
    

class UpdatePostView(LoginRequiredMixin,generic.UpdateView):

    template_name = 'base/update_post.html'
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('index')


    def form_valid(self, form):
        self.object = form.save(commit=False)

        self.object.created_by = self.request.user
        if 'draft' in self.request.POST:
            self.object.is_draft = True

        if 'create' in self.request.POST:
            self.object.is_draft = False

            
        self.object.save()

        return super().form_valid(form)
    

    def dispatch(self, request,*args, **kwargs):
        if request.user.user_type == 1:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)






class MyPostView(LoginRequiredMixin,generic.ListView):

    template_name = 'base/my_posts.html'
    model = Post
    context_object_name = 'posts'

    def get_queryset(self):

        return Post.objects.filter(Q(created_by = self.request.user) &
                                   
                                   (Q(is_draft =False))
                                   )


    def dispatch(self, request,*args, **kwargs):
        if request.user.user_type == 1:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class AppointmentView(LoginRequiredMixin,generic.ListView):

    template_name = 'base/appointment.html'
    model = User

    context_object_name = 'doctors'

    def get_queryset(self):

        return User.objects.filter(user_type = 2)
    

    
class BookAppointmentView(LoginRequiredMixin,generic.CreateView):
    model = User
    template_name = 'base/book_appointment.html'
    form_class = AppointmentForm
   

    def form_valid(self, form,**kwargs):
        doctor = User.objects.get(id = self.kwargs['pk'])

        self.object = form.save(commit=False)
        # self.object.end_time = self.object.start_time + datetime.timedelta(minutes=45)

        start_time = self.object.start_time 
        end_time =  datetime.datetime(1970, 1, 1, start_time.hour, start_time.minute, start_time.second, start_time.microsecond) + datetime.timedelta(minutes=45)
        self.object.end_time = datetime.time(end_time.hour, end_time.minute, end_time.second, end_time.microsecond)
        self.object.doctor_name = doctor.first_name + " " + doctor.last_name
        self.object.doctor_email = doctor.email
        self.object.save()

        
       

        service.events().insert(
        calendarId="primary",
        body={
            "summary": self.object.require,
        
            "start": {"dateTime": str(self.object.date)+"T"+str(start_time),
            'timeZone': "Asia/Kolkata",
        
        
        },
            "end": {
                "dateTime": str(self.object.date)+"T"+str(self.object.end_time),
                   'timeZone': "Asia/Kolkata",
            },
            "attendees":[{"email":self.object.doctor_email}
        
        ]
    },
).execute()

        return redirect('appointment-detail',pk= self.object.id)
   

class AppointmentDetailView(LoginRequiredMixin,generic.DetailView):
    model = Appointment
    template_name = 'base/appointment_detail.html'
    context_object_name = 'appointment'

    





