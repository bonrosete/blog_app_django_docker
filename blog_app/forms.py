from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='username', max_length=45)
    password = forms.CharField(widget=forms.PasswordInput)

class SignupForm(forms.Form):
    username = forms.CharField(label='username', max_length=45)
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    check_password = forms.CharField(label='verify password', widget=forms.PasswordInput)
    first_name = forms.CharField(label='first name', max_length=45)
    last_name = forms.CharField(label='last name', max_length=45)
    age = forms.IntegerField(label='age', widget=forms.NumberInput, max_value=100, min_value=1)
    gender = forms.ChoiceField(choices=(('M', 'Male'), ('F', 'Female')))