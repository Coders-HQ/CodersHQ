# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from .forms import ProfileCreateForm
from django.urls import reverse
from .models import Portfolio

@login_required
def create_profile(request):

    profile = None
    try:
        profile = Portfolio.objects.get(user=request.user)
    except:
        pass

    if profile==None:
        if request.method == 'POST':
            form = ProfileCreateForm(request.POST)
            if form.is_valid():
                profile = form.save(commit=False)
                profile.user = request.user
                profile.save()

                return redirect("users:plural", username=request.user.username)

        form = ProfileCreateForm()
        return render(request, "assessment/profile_form.html", {"form": form})
    
    else:
        return redirect("users:plural", username=request.user.username)