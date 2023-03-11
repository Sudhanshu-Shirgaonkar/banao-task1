from django.contrib.auth.forms import UserCreationForm
from .models import User
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