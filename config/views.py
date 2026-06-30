from django.http import JsonResponse

def home(request):
    return JsonResponse({
        "message": "Subscription SaaS Backend API",
        "status": "Running",
        "version": "1.0",
        "developer": "Anuj Kushwaha",
        "apis": {
            "signup": "/api/signup/",
            "login": "/api/login/",
            "plans": "/api/plans/",
            "profile": "/api/profile/",
            "subscribe": "/api/subscribe/",
            "subscription": "/api/subscription/"
        }
    })