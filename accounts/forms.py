from django import forms
from django.contrib.auth import get_user_model
from .models import Profile

User = get_user_model()

class UserRegisterForm(forms.ModelForm):
    password1   = forms.CharField(label='Password',widget=forms.PasswordInput)
    password2   = forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def clean_passowrd2(self):
        pwrd1 = self.cleaned_data.get('password1')
        pwrd2 = self.cleaned_data.get('password2')
        if pwrd1 and pwrd2 and pwrd1!=pwrd2:
            raise forms.Validation('Passwords must MatcH!!!')
        return pwrd2

    def clean(self,*args,**kwargs):
        email = self.cleaned_data.get('email')
        qs  = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Email already taken!')
        return super(UserRegisterForm,self).clean(*args,**kwargs)


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name',)

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo','dob',)
