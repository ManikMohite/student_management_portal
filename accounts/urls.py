from django.urls import path
from . import views

urlpatterns = [

    path("", views.login_view, name="login"),
path("register/", views.register_student, name="register"),
    path("logout/", views.logout_view, name="logout"),

    path(
        "dashboard/",
        views.admin_dashboard,
        name="admin_dashboard"
    ),

]