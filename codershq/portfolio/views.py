from django.shortcuts import render
from .forms import PortfolioForm


def public(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST' and 'github_url' in request.POST:
        # create a form instance and populate it with data from the request:
        form = PortfolioForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            print("success")
        else:
            print(form.errors)

    # if a GET (or any other method) we'll create a blank form
    else:
        return render(request, 'portfolio/portfolio_form.html')

    print(request.POST)
    return render(request, 'portfolio/portfolio_form.html')
