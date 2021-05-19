from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class User(AbstractUser):

    class Branch(models.TextChoices):
        CSE = 'CSE'
        IT = 'IT'
        ECE = 'ECE'
        EEE = 'EEE'
        MECH = 'MECH'
        CIVIL = 'CIVIL'
        CHEM = 'CHEM'

    class Section(models.IntegerChoices):
        I = 1
        II = 2
        III = 3
        IV = 4

    class Semester(models.IntegerChoices):
        I = 1
        II = 2
        III = 3
        IV = 4
        V = 5
        VI = 6
        VII = 7
        VIII = 8

    username = models.CharField(
        max_length=254,
        unique=False
    )
    email = models.EmailField(
        max_length=254, unique=True, null=False, blank=False,
        help_text=_(
            'Enter your institute\'s domain email-id.'),
        error_messages={
            'unique': _("A user with that email already exists."),
        },
    )
    roll_number = models.CharField(max_length=10, null=True, blank=True, unique=True, help_text=_(
        'Enter the roll number assigned by your institute.'), error_messages={'unique': _("A student with that roll number already exists.")},)
    branch = models.CharField(
        max_length=5, choices=Branch.choices, null=False, blank=False,
        help_text=_(
            'Select the engineering branch you study or teach.'),
    )
    section = models.IntegerField(
        choices=Section.choices, null=True, blank=True,
        help_text=_(
            'Mention your section.'),)
    semester = models.IntegerField(
        choices=Semester.choices, null=True, blank=True,
        help_text=_(
            'Provide your semester (not year).'))
    image = models.ImageField(verbose_name="Profile Pic", default="default.jpg", upload_to="profile_pics",
                              help_text=_(
                                  'This will be your display image.'),
                              )

    objects = CustomUserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['branch']

    class Meta:
        ordering = ['email']

    def is_student(self):
        return (not self.is_staff) and (not self.is_superuser)

    def is_faculty(self):
        return self.is_staff and (not self.is_superuser)

    def is_admin(self):
        return self.is_superuser

    def __str__(self):
        return f'{self.email}\'s Profile'
