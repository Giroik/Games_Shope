from django.urls import path
import django.contrib.auth.views as auth_views
from accounts.views import UserCreationView

urlpatterns=[
    path('login/', auth_views.LoginView.as_view(),name="login"),
    path('logout/', auth_views.LogoutView.as_view(),name="logout"),
    path('singup/', UserCreationView.as_view(),name="singup"),
    path('password_change/',auth_views.PasswordChangeView.as_view(),name="password_change"),
    path('password_change_done/', auth_views.PasswordChangeDoneView.as_view(), name="password_change_done")

]
#получаем представление оформе с помощю готового класса LoginView.

