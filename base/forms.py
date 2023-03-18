from django.contrib.auth.forms import UserCreationForm
from .models import User,Post,Appointment
from django import forms


class MyUserCreationForm(UserCreationForm):

    class Meta:

        model = User
        fields = ['first_name','last_name','profile_picture','username','email','password1','password2','address']

        widgets = {
            'address': forms.Textarea(attrs={'rows':4, 'cols':30, 'class':'form-control'}),
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
        
        }

    def __init__(self, *args, **kwargs):
        super(MyUserCreationForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None






class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title','post_image','category','summary','content']

        widgets = {
            
            'title':forms.TextInput(attrs={'class':'form-control', 'id':'title'}),
            'summary': forms.Textarea(attrs={'rows':4, 'cols':30, 'class':'form-control','id':'summary'}),
            'content': forms.Textarea(attrs={'rows':4, 'cols':30, 'class':'form-control','id':'content'}),
            'category':forms.Select(attrs={'class':'form-control'})
        }





class AppointmentForm(forms.ModelForm):

    class Meta:

        model = Appointment
        exclude = ['end_time','doctor_name','doctor_email']


        widgets = {
            
            'require':forms.TextInput(attrs={'class':'form-control', 'id':'title'}),
            'date': forms.TextInput(attrs={ 'type':'date','class':'form-control'}),
            'start_time': forms.TextInput(attrs={'type':'time','class':'form-control','id':'content'}),
            'category':forms.Select(attrs={'class':'form-control'})
        }


        