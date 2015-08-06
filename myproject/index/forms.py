from django import forms
from django .contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MyRegistrationForm(UserCreationForm):
        email = forms.EmailField(required=True)
        first_name = forms.CharField(max_length=20)
        last_name = forms.CharField(max_length=20)
        class Meta:
                model = User
                fields = ('username',
                          'first_name',
                          'last_name',
                          'email',
                          'password1',
                          'password2')
                
        def save(self, commit=True):
            user = super(MyRegistrationForm, self).save(commit=False)
            user.email = self.cleaned_data['email']

            if commit:
                user.save()

            return user

