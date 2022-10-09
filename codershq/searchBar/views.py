from django.shortcuts import render

def searchBar(request):
    return render(request, 'pages/searchBar.html', {})
