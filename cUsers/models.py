from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# class User(AbstractUser):
#     class Types(models.TextChoices):
#         EMPLOYEE = "EMPLOYEE", "Employee"
#         EMPLOYER = "EMPLOYER", "Employer"
#
#     base_type = Types.EMPLOYER
#
#     # What type of user are we?
#     type = models.CharField(
#         _("Type"), max_length=50, choices=Types.choices, default=base_type
#     )
#
#     # First Name and Last Name Do Not Cover Name Patterns
#     # Around the Globe.
#     name = models.CharField(_("Name of User"), blank=True, max_length=255)
#
#     # def get_absolute_url(self):
#     #     return reverse("users:detail", kwargs={"username": self.username})
#
#     def save(self, *args, **kwargs):
#         if not self.id:
#             self.type = self.base_type
#         return super().save(*args, **kwargs)
#
#
# class EmployeeManager(models.Manager):
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter(type=User.Types.EMPLOYEE)
#
#
# class EmployerManager(models.Manager):
#     def get_queryset(self, *args, **kwargs):
#         return super().get_queryset(*args, **kwargs).filter(type=User.Types.EMPLOYER)
#
#
# class EmployeeMore(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     about = models.TextField()
#
#
# class Employee(User):
#     base_type = User.Types.EMPLOYEE
#     objects = EmployeeManager()
#
#     class Meta:
#         proxy = True
#
#     def employeeFunc(self):
#         return "Employee"
#
#
# class EmployerMore(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     model = models.CharField(max_length=255)
#     make = models.CharField(max_length=255)
#     year = models.IntegerField()
#
#
# class Employer(User):
#     base_type = User.Types.EMPLOYER
#     objects = EmployerManager()
#
#     @property
#     def more(self):
#         return self.EmployerMore
#
#     class Meta:
#         proxy = True
#
#     def EmployerFunc(self):
#         return "Go Employer"

############################################################################################################################
# if the users can assume only one role, you could have a choices field like
# This way you have a central point to check what is the type of the user. Usually using boolean flags works better!
class User(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Employer'),
        (2, 'Employee'),
        (3, 'secretary'),
        (4, 'supervisor'),
        # (5, 'admin'),
    )

    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, blank=True, null=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    username = models.CharField(max_length=250, unique=True)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.type = self.user_type
    #     return super().save(*args, **kwargs)


class Recruiter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.PositiveIntegerField(null=True, blank=True)
    company_name = models.CharField(max_length=150, null=True, blank=True)
    company_description = models.CharField(max_length=300, null=True, blank=True)
    website = models.CharField(max_length=100, default="")

    def __str__(self):
        return f"{self.user.username} {self.company_name} "


class Applicant(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} {self.user.age} "


# secretary

class Secretary(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} {self.user.age} "


# supervisor
class Supervisor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone_number = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} {self.user.age} "
############################################################################################################################
# If your application handle many user types, and users can assume multiple roles,
# an option is to create an extra table and create a many to many relationship:
# In this case I created some constants inside the Role model,
#  so you can define behavior in the application using those constant values like if role == Role.ADMIN:.

# class Role(models.Model):
#     """
#     The Role entries are managed by the system,
#     automatically created via a Django data migration.
#     """
#     EMPLOYER = 1
#     EMPLOYEE = 2
#     SECRETARY = 3
#     SUPERVISOR = 4
#     ADMIN = 5
#     ROLE_CHOICES = (
#         (EMPLOYER, 'Employer'),
#         (EMPLOYEE, 'Employee'),
#         (SECRETARY, 'secretary'),
#         (SUPERVISOR, 'supervisor'),
#         (ADMIN, 'admin'),
#     )
#
#     id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)
#
#     def __str__(self):
#         return self.get_id_display()
#
#
# class User(AbstractUser):
#     roles = models.ManyToManyField(Role)
