from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class Classroom(models.Model):

    name = models.CharField(max_length=35, null=False, blank=False,
                            unique=True,
                            help_text=_(
                                'Enter any valid classroom name. It is usually contains branch name, section and subject.'),
                            error_messages={
                                'unique': _("A classroom with that name already exists."),
                            },
                            )
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    students = models.ManyToManyField(User, related_name='classrooms')

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'Classroom {self.name}'
