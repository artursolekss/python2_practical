from django.urls import path

from . import views

app_name = "spotify"

urlpatterns = [
    # path('', name='index'),
    path("login/",views.LoginView.as_view(),name="login"),
    path("login_run/",views.login_run,name="login_run"),
    path("login_callback",views.login_callback,name="login_callback"),
    path('generate_token',views.generate_token,name="generate_token")
]