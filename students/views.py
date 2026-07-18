from django.shortcuts import render,redirect,get_object_or_404

from .models import Student

from .forms import StudentForm

from django.contrib.auth.decorators import login_required


from django.shortcuts import render, redirect
from .models import Student
from django.contrib.auth.decorators import login_required

@login_required
def student_dashboard(request):

    student = Student.objects.filter(user=request.user).first()

    if student is None:
        return redirect("login")

    return render(
        request,
        "students/dashboard.html",
        {
            "student": student
        }
    )

@login_required
def student_dashboard(request):
    student = get_object_or_404(Student, user=request.user)

    return render(
        request,
        "students/dashboard.html",
        {"student": student}
    )
@login_required
def student_list(request):

    search = request.GET.get("search")

    if search:

        students = Student.objects.filter(

            user__first_name__icontains=search

        )

    else:

        students = Student.objects.all()

    return render(

        request,

        "students/student_list.html",

        {"students":students}

    )
@login_required
def edit_student(request,id):

    student = get_object_or_404(Student,id=id)

    form = StudentForm(instance=student)

    if request.method=="POST":

        form = StudentForm(

            request.POST,

            request.FILES,

            instance=student

        )

        if form.is_valid():

            form.save()

            return redirect("student_list")

    return render(

        request,

        "students/edit_student.html",

        {"form":form}

    )
@login_required
def delete_student(request,id):

    student = get_object_or_404(Student,id=id)

    if request.method=="POST":

        student.delete()

        return redirect("student_list")

    return render(

        request,

        "students/delete_student.html",

        {"student":student}

    )