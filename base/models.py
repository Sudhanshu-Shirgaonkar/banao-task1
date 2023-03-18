from django.db import models

from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Patient'),
        (2, 'Doctor')
    )

    profile_picture = models.ImageField(default="profile_pics/avatar.svg",upload_to='profile_pics')
    address = models.TextField(help_text='(line1, city, state, pincode)',max_length=500)
 
    user_type = models.PositiveIntegerField(choices=USER_TYPE_CHOICES,default=1)



class Post(models.Model):
    USER_TYPE_CHOICES = (
        ('Mental Health', 'MENTAL HEALTH'),
        ('Heart Disease', 'HEART DESEASE'),
        ('Covid 19','COVID 19'),
        ('Immunization','IMMUNIZATION')
    )

    created_by = models.ForeignKey(User, on_delete= models.CASCADE)
    title = models.CharField(max_length= 100)
    post_image = models.ImageField(default="post_pics/defaul.jpeg",upload_to='post_pics')
    category =  models.CharField(max_length=100,choices= USER_TYPE_CHOICES,default= 'Mental Halth')
    summary = models.TextField()
    content = models.TextField()
    is_draft = models.BooleanField(default=False)
    is_saved = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True) 
    created = models.DateTimeField(auto_now_add=True)

    class Meta:

        ordering = ['-created']


    def __str__(self):

        return self.title
        

class Appointment(models.Model):

    require = models.CharField(max_length=100)
    doctor_name =  models.CharField(max_length=100)
    doctor_email = models.CharField(max_length=100)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()


    def __str__(self):

        return self.require




