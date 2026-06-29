from django.urls import path
from .views import LoginView, SignupView, ProfileView, DashboardView, PremiumContentView

urlpatterns = [
    path("signup/", SignupView.as_view(), name="signup"),
    path("login/", LoginView.as_view(), name="login"),
    path("profile/", ProfileView.as_view()),
    path("dashboard/", DashboardView.as_view()),
    path("premium-content/", PremiumContentView.as_view()),
]