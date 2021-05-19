from classrooms.models import Classroom
from django.contrib import messages
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import UserRegistrationForm

User = get_user_model()


def register(request):
    if request.user.is_authenticated:
        messages.info(
            request, f'You can\'t create an account while you are logged in.')
        return redirect('dashboard')
    if request.method == "POST":
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            user = authenticate(email=form.cleaned_data['email'],
                                password=form.cleaned_data['password1'],
                                )
            login(request, user)
            email = form.cleaned_data.get('email')
            messages.success(
                request, f'Account created for {email.lower()}. You are now logged in.')
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def dashboard(request):
    user = User.objects.get(pk=request.user.id)
    classrooms = Classroom.objects.all()

    return render(request, 'users/dashboard.html', {'user': user, 'classrooms': classrooms})


@login_required
def profile(request):
    user = User.objects.get(pk=request.user.id)

    return render(request, 'users/profile.html', {'user': user})
