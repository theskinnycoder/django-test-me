from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserRegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2',
                  'roll_number', 'is_staff', 'branch', 'section', 'semester', 'image']
        labels = {
            "is_staff": _("Are you faculty or staff?")
        }

        help_texts = {
            "is_staff": _("Only faculty can create classrooms and tests")
        }
