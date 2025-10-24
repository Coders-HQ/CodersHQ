from django.shortcuts import redirect, render
from django.http import JsonResponse
from codershq.users.forms import UserInterestForm
from codershq.users.models import UserInterest

def index(request):
    if not request.user.is_authenticated:
        return redirect("/accounts/login/")

    instance, created = UserInterest.objects.get_or_create(user=request.user)

    # ✅ Handle AJAX POST (inside modal)
    if request.method == "POST" and request.headers.get("x-requested-with") == "XMLHttpRequest":
        form = UserInterestForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            message = "✅ Interests registered successfully." if created else "✅ Interests updated successfully."
            return JsonResponse({"message": message})
        return JsonResponse({"errors": form.errors}, status=400)

    # GET: Render base page with button
    form = UserInterestForm()
    return render(request, "_dashboard.html", {"form": form})


def landing(request):
    return render(request, "pages/welcome.html")


def news(request):
    resp = requests.get(url=news_url, headers={"User-agent": "your bot 0.1"})
    body = resp.json()
    context = {"body": body["data"]["children"]}
    return render(request, "dashboard/news.html", context)
