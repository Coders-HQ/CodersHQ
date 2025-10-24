from django.conf import settings
from django.views.generic import TemplateView
from djangosaml2idp.models import ServiceProvider
from .forms import AssessmentForm 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

class IndexView(TemplateView):
    template_name = "assessment/index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context.update({
            "logout_url": settings.LOGOUT_URL,
            "login_url": settings.LOGIN_URL,
        })
        if self.request.user.is_authenticated:
            context.update({
                "known_sp_ids": [sp for sp in ServiceProvider.objects.filter(active=True)],
            })
        return context
    #added assessment function
@login_required
def assessment_form(request):
    if request.method == 'POST':
        print("Form POST submitted")
        profile_form = AssessmentForm(request.POST)
        if profile_form.is_valid():
            print("Form is valid")
            assessment = profile_form.save(commit=False)
            assessment.user = request.user
            assessment.save()
            print("Redirecting to dashboard:home")
            return redirect('dashboard:home')  # or use reverse()
        else:
            print("Form is invalid:")
            print(profile_form.errors)
    else:
        profile_form = AssessmentForm()

    return render(request, 'assessment/plural_password.html', {
        'profile_form': profile_form
    })
