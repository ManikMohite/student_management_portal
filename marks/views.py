from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Mark
from .forms import MarkForm
from students.models import Student


@login_required
def mark_list(request):

    marks = Mark.objects.all()

    return render(
        request,
        "marks/mark_list.html",
        {"marks": marks}
    )


@login_required
def add_mark(request):

    form = MarkForm()

    if request.method == "POST":

        form = MarkForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("mark_list")

    return render(
        request,
        "marks/add_mark.html",
        {"form": form}
    )


@login_required
def edit_mark(request, id):

    mark = get_object_or_404(Mark, id=id)

    form = MarkForm(instance=mark)

    if request.method == "POST":

        form = MarkForm(request.POST, instance=mark)

        if form.is_valid():

            form.save()

            return redirect("mark_list")

    return render(
        request,
        "marks/add_mark.html",
        {"form": form}
    )


@login_required
def delete_mark(request, id):

    mark = get_object_or_404(Mark, id=id)

    mark.delete()

    return redirect("mark_list")


@login_required
def student_marks(request):

    student = Student.objects.get(user=request.user)

    marks = Mark.objects.filter(student=student)

    return render(
        request,
        "marks/student_marks.html",
        {"marks": marks}
    )