from django import forms
from django.contrib.auth.models import User

class UserCreationForm(forms.ModelForm):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Username'}),
        required=True
    )

    email = forms.EmailField(
        max_length=150,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter Your Email'}),
        required=True
    )

    password = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Password'}),
        required=True
    )

    password2 = forms.CharField(
        max_length=128,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Your Confirm Password'}),
        required=True
    )
    
    class Meta:
        model = User
        fields = (
            'username','email','password','password2'
        )
    
    def clean(self):
        cleaned_data =  super().clean()
        password = cleaned_data.get("password","")
        password2 = cleaned_data.get("password2","")
        
        if not password or not password2:
            raise forms.ValidationError("you must set your password.")
        
        if len(password)<8:
            raise forms.ValidationError("your password must be at least 8 char.")
        
        if password != password2:
            raise forms.ValidationError("your password must be same with confirm password")
        
        return cleaned_data
    
    def save(self, commit = ...):
        user =  super().save(commit = False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user