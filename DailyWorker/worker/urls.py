from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("profile", views.profile, name="profile"),
    path("rent", views.rent, name="rent"),
    path("reserve/<int:toolid>", views.reserve, name="reserve"),
    path("borrow/<int:toolid>", views.borrow, name="borrow"),
    path("seeker", views.seeker, name="seeker"),
    path("search", views.search, name="search"),
    path("worker", views.worker, name="worker"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    ]