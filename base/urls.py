
from django.urls import path
from .import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("", views.IndexView.as_view(),name= 'index'),
    path("login/",views.LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path("register/",views.RegisterView.as_view(),name='register'),
    path("register/doctor/",views.DoctorRegisterView.as_view(),name='doctor_register'),
    path("register/patient/",views.PatientRegisterView.as_view(),name='patient_register'),
    path('profile/<str:pk>/',views.ProfileView.as_view(),name='profile'),
    path('edit-profile/<str:pk>/',views.EditProfileView.as_view(),name='edit-profile'),
 
]
