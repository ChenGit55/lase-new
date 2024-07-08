from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def home_view(request):
    return render(request, "home.html", context={})


@csrf_exempt
def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        msg = request.POST.get("msg")

        send_mail(
            subject=f"Contact message from {name} - {email}, sent by web site.",
            message=msg,
            from_email=email,
            recipient_list=["xegei_cps@hotmail.com"],
        )

        if request.headers.get("X-Requested-With") == "XMLHttpRequest":
            return JsonResponse({"message": "SUCCESS"})
        else:
            return render(request, "contact.html")

    context = {}
    return render(request, "contact.html", context)
