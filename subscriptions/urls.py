from django.urls import path
from .views import SubscribeView,UpgradePlanView,CancelSubscriptionView,CurrentSubscriptionView

urlpatterns = [
    path("subscribe/", SubscribeView.as_view(), name="subscribe"),
    path("upgrade-plan/",UpgradePlanView.as_view(), name="upgrade-plan"),
    path("cancel-subscription/", CancelSubscriptionView.as_view()),
    path("subscription/", CurrentSubscriptionView.as_view()),
]