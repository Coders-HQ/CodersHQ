import requests
from django.shortcuts import redirect, render

news_url = "https://www.reddit.com/r/programming/.json"


def index(request):
    if not request.user.is_authenticated:
        return redirect("/accounts/login/")
    return redirect("/accounts/login/")
    # return render(request, "pages/dashboard.html")


def landing(request):
    return render(request, "pages/welcome.html")


def news(request):
    resp = requests.get(url=news_url, headers={"User-agent": "your bot 0.1"})
    body = resp.json()
    context = {"body": body["data"]["children"]}
    return render(request, "dashboard/news.html", context)
