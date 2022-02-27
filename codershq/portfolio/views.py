from django.shortcuts import render


def public(request):

    return render(request, "portfolio/public.html")