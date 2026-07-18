from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import LoginForm
from students.models import Student
from attendance.models import Attendance
from marks.models import Mark


from django.contrib.auth.models import User
from .forms import StudentRegistrationForm



def login_view(request):

    # If user is already logged in
    if request.user.is_authenticated:

        if request.user.is_superuser:
            return redirect("admin_dashboard")

        if Student.objects.filter(user=request.user).exists():
            return redirect("student_dashboard")

        logout(request)

    form = LoginForm()

    if request.method == "POST":

        form = LoginForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(
                username=username,
                password=password
            )

            if user is not None:

                login(request, user)

                # Admin Login
                if user.is_superuser:
                    return redirect("admin_dashboard")

                # Student Login
                if Student.objects.filter(user=user).exists():
                    return redirect("student_dashboard")

                # User exists but no Student profile
                logout(request)

                return render(
                    request,
                    "accounts/login.html",
                    {
                        "form": form,
                        "error": "Student profile not found."
                    }
                )

            else:

                return render(
                    request,
                    "accounts/login.html",
                    {
                        "form": form,
                        "error": "Invalid Username or Password"
                    }
                )

    return render(
        request,
        "accounts/login.html",
        {"form": form}
    )


@login_required
def logout_view(request):

    logout(request)

    return redirect("login")


@login_required
def admin_dashboard(request):

    context = {

        "students": Student.objects.count(),

        "attendance": Attendance.objects.count(),

        "marks": Mark.objects.count(),

    }

    return render(
        request,
        "admin/dashboard.html",
        context
    )


def register_student(request):

    if request.method == "POST":

        form = StudentRegistrationForm(request.POST)

        if form.is_valid():

            data = form.cleaned_data

            if User.objects.filter(username=data["username"]).exists():
                form.add_error("username", "Username already exists")
            else:

                user = User.objects.create_user(
                    username=data["username"],
                    password=data["password"],
                    first_name=data["first_name"],
                    last_name=data["last_name"],
                )

                Student.objects.create(
                    user=user,
                    roll_no=data["roll_no"],
                    department=data["department"],
                    semester=data["semester"],
                    phone=data["phone"],
                    address=data["address"],
                )

                return redirect("login")

    else:
        form = StudentRegistrationForm()

    return render(
        request,
        "accounts/register.html",
        {"form": form},
    )