from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import ApplicantCustomUserCreationForm,\
    RecruiterCustomUserCreationForm,\
    SecretaryCustomUserCreationForm, \
    SupervisorCustomUserCreationForm

# Create your views here.
from .models import User


class RecruiterSignUpView(CreateView):
    model = User
    form_class = RecruiterCustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/employer_signup.html'


class ApplicantSignUpView(CreateView):
    model = User
    form_class = ApplicantCustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/emplyee_signup.html'


# SecretarySignUpView

class SecretarySignUpView(CreateView):
    model = User
    form_class = SecretaryCustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/secretary_signup.html'


# SupervisorSignUpView
class SupervisorSignUpView(CreateView):
    model = User
    form_class = SupervisorCustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/supervisor_signup.html'

#
# class customer_register(CreateView):
#     model = User
#     form_class = CustomerSignUpForm
#     template_name = '../templates/customer_register.html'
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('/')
#
#
# class employee_register(CreateView):
#     model = User
#     form_class = EmployeeSignUpForm
#     template_name = '../templates/employee_register.html'
#
#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('/')
