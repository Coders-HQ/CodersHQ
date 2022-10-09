from django.shortcuts import render, redirect
from codershq.portfolio.models.model_portfolio import Education
from django.urls import reverse

from codershq.portfolio.models.model_project import Project

from .forms import (PortfolioForm, 
                    EducationForm, 
                    UserForm, 
                    ExperienceForm, 
                    ProjectForm,
                    LanguageForm,
                    AwardForm)
from django.contrib.auth.decorators import login_required
from .models import Portfolio, Experience, Award, Language
from django.shortcuts import get_object_or_404
from codershq.users.models import User

@login_required
def portfolio_edit(request):

    # create portfolio if user doesnt have it
    user = request.user
    try:
        portfolio = Portfolio.objects.get(user=user)
        print("user had portfolio")
    except Portfolio.DoesNotExist:
        portfolio = Portfolio()
        portfolio.user = user
        portfolio.save()
        print("save user portfolio")

    # if this is a POST request we need to process the form data
    if request.method == 'POST':

        # choose the right form
        if 'github_url' in request.POST:
            # create a form instance and populate it with data from the request:
            form = PortfolioForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                data = form.cleaned_data
                portfolio.twitter_handle = data['twitter_handle']
                portfolio.github_url = data['github_url']
                portfolio.website_url = data['website_url']
                portfolio.linkedin_url = data['linkedin_url']
                portfolio.description = data['description']
                # save to database
                portfolio.save()
            else:
                print(form.errors)

        if 'education_school' in request.POST:
            form = EducationForm(request.POST)
            if form.is_valid():
                education = Education()
                data = form.cleaned_data
                education.user_profile = portfolio
                education.school = data['education_school']
                education.degree = data['education_degree']
                education.start_date = data['education_start_date']
                education.end_date = data['education_end_date']
                education.save()
            else:
                print(form.errors)

        if 'name' in request.POST:
            form = UserForm(request.POST, request.FILES)
            if form.is_valid():
                data = form.cleaned_data
                user.name = data['name']
                user.bio = data['about']
                user.profile_image = data['profile_image']
                user.save()

            else:
                print(form.errors)

        if 'job_title' in request.POST:
            form = ExperienceForm(request.POST)
            if form.is_valid():
                experience = Experience()
                data = form.cleaned_data
                experience.user_profile = portfolio
                experience.job_title = data['job_title']
                experience.start_date = data['start_date']
                experience.end_date = data['end_date']
                experience.is_current = data['is_current']
                experience.save()

            else:
                print(form.errors)

        if 'project_name' in request.POST:
            form = ProjectForm(request.POST)
            if form.is_valid():
                project = Project()
                data = form.cleaned_data
                project.user_profile = portfolio
                project.name = data['project_name']
                project.description = data['project_description']
                project.link = data['project_url']
                project.save()

            else:
                print("project form not success")
                print(form.errors)

        if 'award_name' in request.POST:
            form = AwardForm(request.POST)
            if form.is_valid():
                award = Award()
                data = form.cleaned_data
                award.user_profile = portfolio
                award.name = data['award_name']
                award.date_awarded = data['award_date_awarded']
                award.save()

            else:
                print(form.errors)

        if 'language_name' in request.POST:
            form = LanguageForm(request.POST)
            if form.is_valid():
                language = Language()
                data = form.cleaned_data
                language.user_profile = portfolio
                language.name = data['language_name']
                language.proficiency = data['language_proficiency']
                language.save()

            else:
                print(form.errors)

    print(request.POST)
    context = {"portfolio": portfolio}
    return render(request, 'portfolio/portfolio_form.html', context)


def portfolio_show(request, username):
    user = get_object_or_404(User, username=username)
    context = {'user': user}
    portfolio = Portfolio.objects.get(user=user)
    context['portfolio'] = portfolio
    educations = Education.objects.all().filter(user_profile=portfolio)
    experiences = Experience.objects.all().filter(user_profile=portfolio)
    projects = Project.objects.all().filter(user_profile=portfolio)
    award = Award.objects.all().filter(user_profile=portfolio)
    context['educations'] = educations
    return render(request, 'portfolio/portfolio.html', context)

def portfolio_language_delete(request, pk):
    language = get_object_or_404(Language, pk=pk)
    Language.delete(language)
    return redirect(reverse('portfolio:edit_portfolio'))

def portfolio_award_delete(request, pk):
    award = get_object_or_404(Award, pk=pk)
    Award.delete(award)
    return redirect(reverse('portfolio:edit_portfolio'))
