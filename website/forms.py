from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms
from .models import Book
from .models import CustomeUser,Student


from django import forms
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}))
    first_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}))
    is_admin = forms.BooleanField(label="Is Admin", required=False)  # Add the is_admin field

    class Meta:
        model = CustomeUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'is_admin')  # Include is_admin in the fields list

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'










from django import forms
from .models import Book

class AddRecord(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Title", "class": "form-control"}), label="")
    author = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Author", "class": "form-control"}), label="")
    year_of_publish = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder": "Year of Publish", "class": "form-control"}), label="")
    is_borrowed = forms.BooleanField(
        required=False,
        initial=False,
        widget=forms.widgets.CheckboxInput(attrs={"style": "width: 20px; height: 20px; background-color: #007bff; border: 1px solid #007bff; border-radius: 3px;"}),
        label="Is Borrowed"
    )

    class Meta:
        model = Book
        exclude = ("user",)  # Exclude any fields you don't want to include in the form






from django import forms
from .models import Student

class StudentRegistrationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'username',
            'first_name',
            'last_name',
            'phone_number',
            'email',
            'address',
            'city',
            'state',
            'zip_code',
            'password',
        ]
        widgets = {
            'password': forms.PasswordInput(),  # To hide the password input
        }




# forms.py
from django import forms

class CustomLoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
