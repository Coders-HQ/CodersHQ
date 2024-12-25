import requests
from django.shortcuts import redirect, render
from django.http import HttpResponse

# Reddit API URL
news_url = "https://www.reddit.com/r/programming/.json"

def index(request):
    """
    Redirects to login page if the user is not authenticated.
    """
    if not request.user.is_authenticated:
        return redirect("/accounts/login/")
    return render(request, "pages/dashboard.html")


def landing(request):
    """
    Renders the welcome landing page.
    """
    return render(request, "pages/welcome.html")


def news(request):
    """
    Fetches news from Reddit's programming subreddit and renders the news page.
    """
    try:
        # Fetch data from Reddit
        resp = requests.get(news_url, headers={"User-agent": "your bot 0.1"})
        resp.raise_for_status()  # Raises an HTTPError for bad responses
        
        # Parse the JSON response
        body = resp.json()
        context = {
            "body": body["data"]["children"]
        }

        return render(request, "dashboard/news.html", context)

    except requests.exceptions.RequestException as e:
        # If there is any issue with the request, return an error message
        return HttpResponse(f"An error occurred while fetching news: {str(e)}", status=500)
