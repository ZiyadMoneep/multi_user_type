from django import forms
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Recruiter, Applicant, User


class ApplicantCustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        help_text="Enter Your first name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}),
    )

    last_name = forms.CharField(
        max_length=100,
        required=True,
        help_text="Enter Your last name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}),
    )

    username = forms.CharField(
        max_length=100,
        required=True,
        help_text="Enter Your username",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
    )
    phone_number = forms.NumberInput()
    age = forms.IntegerField(help_text="Enter Your age",
                             widget=forms.NumberInput(
                                 attrs={'class': 'form-control', 'placeholder': 'age'}),
                             )
    email = forms.EmailField(
        max_length=100,
        required=True,
        help_text="Enter Your email",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
    )

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'age',)

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_Applicant = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.age = self.cleaned_data.get('age')
        user.save()
        applicant = Applicant.objects.create(user=user)
        applicant.phone_number = self.cleaned_data.get('phone_number')
        applicant.save()
        return user


# class ApplicantCustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm):
#         model = User
#         fields = ('username', 'age', 'email',)


class RecruiterCustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        max_length=100,
        required=True,
        help_text="Enter Your first name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'first name'}),
    )

    last_name = forms.CharField(
        max_length=100,
        required=True,
        help_text="Enter Your last name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'last name'}),
    )

    username = forms.CharField(
        max_length=100,
        required=True,
        help_text="Enter Your username",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}),
    )
    email = forms.EmailField(
        max_length=100,
        required=True,
        help_text="Enter Your email",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'email'}),
    )

    company_name = forms.CharField(
        max_length=250,
        required=True,
        help_text="Enter Your company_name",
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'company_name'}),
    )

    website = forms.CharField(
        max_length=250,
        required=True,
        help_text="Enter Your company website",
        widget=forms.URLInput(attrs={'class': 'form-control', 'placeholder': 'company website'}),
    )

    phone_number = forms.IntegerField(help_text="Enter Your phone number",
                                      widget=forms.NumberInput(
                                          attrs={'class': 'form-control', 'placeholder': 'phone number'}),
                                      )

    age = forms.IntegerField(help_text="Enter Your age",
                             widget=forms.NumberInput(
                                 attrs={'class': 'form-control', 'placeholder': 'age'}),
                             )

    class Meta(UserCreationForm):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'company_name', 'website', 'phone_number')

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_Recruiter = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.username = self.cleaned_data.get('username')
        user.email = self.cleaned_data.get('email')
        user.age = self.cleaned_data.get('age')
        user.save()
        recruiter = Recruiter.objects.create(user=user)
        recruiter.phone_number = self.cleaned_data.get('phone_number')
        recruiter.company_name = self.cleaned_data.get('company_name')
        recruiter.website = self.cleaned_data.get('website')
        recruiter.save()
        return user

# class RecruiterCustomUserChangeForm(UserChangeForm):
#     class Meta(UserChangeForm):
#         model = User
#         fields = ('username', 'age', 'email',)
