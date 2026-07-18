from django.urls import path
from . import views

urlpatterns = [

    path("", views.mark_list, name="mark_list"),

    path("add/", views.add_mark, name="add_mark"),

    path("edit/<int:id>/", views.edit_mark, name="edit_mark"),

    path("delete/<int:id>/", views.delete_mark, name="delete_mark"),

    path("my-marks/", views.student_marks, name="student_marks"),

]