from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import ClassroomCreationForm
from .models import Classroom


def create_classroom(request):
    if not request.user.is_faculty():
        messages.warning(
            request, f'You are a student. You can\'t create a classroom.')
        return redirect('dashboard')
    if request.method == "POST":
        form = ClassroomCreationForm(request.POST)
        if form.is_valid():
            classroom = form.save(commit=False)
            classroom.teacher = request.user
            classroom.save()
            title = form.cleaned_data.get('title')
            messages.success(
                request, f'{name.upper()} classroom created.')
            return redirect('dashboard')
    else:
        form = ClassroomCreationForm()
    return render(request, 'classrooms/create_classroom.html', {'form': form})


def get_classroom(request, id):
    classroom = Classroom.objects.get(pk=id)
    return render(request, 'classrooms/get_classroom.html', {'classroom': classroom})
