from django.urls import path
from . import views

urlpatterns = [
    # Student Dashboard
    path("dashboard/", views.student_dashboard, name="student_dashboard"),

    # Student List
    path("", views.student_list, name="student_list"),

    # Edit Student
    path("edit/<int:id>/", views.edit_student, name="edit_student"),

    # Delete Student
    path("delete/<int:id>/", views.delete_student, name="delete_student"),
]