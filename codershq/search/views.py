from django.shortcuts import render

def search(request):
    if request.method == "POST":
        search = request.POST.get('search', False)
        search_select = request.POST.get('search_select', False)
        return render(request, 'pages/search.html', {'search': search, 'search_select': search_select})
    else:
        return render(request, 'pages/search.html', {})
