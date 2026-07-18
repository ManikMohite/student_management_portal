from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import Attendance
from .forms import AttendanceForm
from students.models import Student


@login_required
def attendance_list(request):

    attendance = Attendance.objects.all().order_by("-date")

    return render(
        request,
        "attendance/attendance_list.html",
        {"attendance": attendance}
    )


@login_required
def add_attendance(request):

    form = AttendanceForm()

    if request.method == "POST":

        form = AttendanceForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("attendance_list")

    return render(
        request,
        "attendance/add_attendance.html",
        {"form": form}
    )


@login_required
def edit_attendance(request, id):

    attendance = get_object_or_404(Attendance, id=id)

    form = AttendanceForm(instance=attendance)

    if request.method == "POST":

        form = AttendanceForm(request.POST, instance=attendance)

        if form.is_valid():

            form.save()

            return redirect("attendance_list")

    return render(
        request,
        "attendance/add_attendance.html",
        {"form": form}
    )


@login_required
def delete_attendance(request, id):

    attendance = get_object_or_404(Attendance, id=id)

    attendance.delete()

    return redirect("attendance_list")


@login_required
def student_attendance(request):

    student = Student.objects.get(user=request.user)

    attendance = Attendance.objects.filter(student=student)

    total = attendance.count()

    present = attendance.filter(status="Present").count()

    percentage = 0

    if total > 0:
        percentage = (present / total) * 100

    context = {
        "attendance": attendance,
        "total": total,
        "present": present,
        "percentage": round(percentage, 2),
    }

    return render(
        request,
        "attendance/student_attendance.html",
        context
    )