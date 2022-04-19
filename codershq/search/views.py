from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.db.models import QuerySet

from codershq.users.models import User
from codershq.events.models import Event

def search(request: HttpRequest) -> HttpResponse:
    if 'search' in request.GET:
        # get the search and search category queries
        search = request.GET.get('search')
        search_category = request.GET.get('search_select')

        # define the context that will be rendered
        context = {
            'search': search,
            'search_select': search_category,
            'contributors_queryset': '',
            'events_queryset': '',
            'skills': [],
        }

        #### Contributors Category ####
        if search_category == "Contributors":
            '''
                Find contributors based on name AND username of registered Users.
                TODO: Filter as per contributor role when integrated with User model.
            '''
            print("INFO: CONTRIBUTORS CATEGORY CHOSEN")

            # get skills query
            skills = request.GET.getlist('skill')
            print("INFO: skills query list received: ", skills)

            # add skills to context
            context['skills'] = skills

            
            contributors_qs = filter_contributors(search_query=search)
            print("INFO: users queryset received: ", contributors_qs)

            # add users queryset to context
            context['contributors_queryset'] = contributors_qs
            

        #### Events Category ####
        # elif search_category == "Events":
        #     print("INFO: EVENTS CATEGORY CHOSEN")

        #     events_qs = filter_events(search_query=search)
        #     print("INFO: events queryset received: ", events_qs)

        #     # add users queryset to context
        #     context['events_queryset'] = events_qs

        #### All Category ####
        else:
            '''
                TODO: display suggestions if no results found
            '''
            print("INFO: ALL CATEGORY CHOSEN")
           
           # get filtered querysets based on search query
            contributors_qs = filter_contributors(search_query=search)
            # events_qs = filter_events(search_query=search)

            # add all querysets to context
            context['contributors_queryset'] = contributors_qs
            # context['events_queryset'] = events_qs
           

        print("INFO: Context sent: ", context)
        return render(request, 'pages/search.html', context)
    else:
        return render(request, 'pages/search.html', {})


def filter_contributors(search_query: str) -> QuerySet:
    # find all registered users
    users_qs = User.objects.all()
    print("INFO: USERS FOUND: ", users_qs)

    # filter found users as per name attribute
    users_qs_name = users_qs.filter(name__icontains=search_query)
    print("INFO: Users filtered as per name: ", users_qs_name)

    # filter found users as per username attribute
    users_qs_username = users_qs.filter(username__icontains=search_query)
    print("INFO: Users filtered as per username: ", users_qs_username)

    # combine the filtered results above
    users_qs = users_qs_name.union(users_qs_username)

    return users_qs

def filter_events(search_query: str) -> QuerySet:
    # find all registered events
    events_qs = Event.objects.all()
    print("INFO: EVENTS FOUND: ", events_qs)

    # filter found events as per title attribute
    events_qs = events_qs.filter(title__icontains=search_query)
    print("INFO: Events filtered as per title: ", events_qs)

    return events_qs
