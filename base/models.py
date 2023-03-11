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



