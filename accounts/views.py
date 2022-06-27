from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import ApplicantCustomUserCreationForm, RecruiterCustomUserCreationForm


# Create your views here.
from .models import User


class RecruiterSignUpView(CreateView):
    model = User
    form_class = RecruiterCustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/employer_signup.html'
    slug_field = "username"
    slug_url_kwarg = "username"




class ApplicantSignUpView(CreateView):
    model = User
    form_class = ApplicantCustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/emplyee_signup.html'
    slug_field = "username"
    slug_url_kwarg = "username"

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