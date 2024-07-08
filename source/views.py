from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse


def home_view(request):
    return render(request, "home.html", context={})


def contact_view(request):
    if request.method == "POST":
        name = request.POST("name")
        email = request.POST("email")
        msg = request.POST("msg")

        send_mail(
            subject=f"Contact message from {name} - {email}, sent by web site.",
            message={msg},
            from_email=email,
            recipient_list=["xegei_cps@hotmail.com"],
        )

        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({"message": "success"})
        else:
            return render(request, "contact.html")

    context = {}
    return render(request, "contact.html", context)


def success_view(request):
    return render(request, "success.html")
