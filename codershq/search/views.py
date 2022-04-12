from django.shortcuts import render

def search(request):
    if 'search' in request.GET:
        search = request.GET.get('search')
        search_select = request.GET.get('search_select')
        return render(request, 'pages/search.html', {'search': search, 'search_select': search_select})
    else:
        return render(request, 'pages/search.html', {})
