
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
    path("create-blog/",views.CreatePostView.as_view(),name='create-blog'),
    path("blog-detail/<str:pk>/",views.BlogDetailView.as_view(),name='blog-detail'),
    path("update-blog/<str:pk>/",views.UpdatePostView.as_view(),name='update-blog'),
    path('edit-profile/<str:pk>/',views.EditProfileView.as_view(),name='edit-profile'),
    path('drafts/',views.DraftView.as_view(),name='draft'),

    path('my-posts/',views.MyPostView.as_view(),name='my-posts'),
 
]
