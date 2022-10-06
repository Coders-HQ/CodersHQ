from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import PluralPasswordForm
import os

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = [
        "name",
        "bio",
        "profile_image",
        "github_profile",
        "academic_qualification",
        "github_profile",
    ]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("portfolio:form")


user_redirect_view = UserRedirectView.as_view()


class UserScoringListView(ListView):
    template_name = "users/scoring_list.html"
    model = User
    context_object_name = "users"
    paginate_by = 50
    ordering = ["-github_score"]


user_scoring_list_view = UserScoringListView.as_view()


@login_required
def plural(request, username):

    # if form is submitted
    if request.method == 'POST':
        password_form = PluralPasswordForm(request.POST)
        home_context = {
            "form": password_form
        }
        if 'password' in request.session:
            if password_form.is_valid():
                password = password_form.cleaned_data['password']
                actual_pw = os.getenv("ASSESSMENT_PASSWORD", default=None)
                if (actual_pw == password):
                    request.session['password'] = 'valid'
                    user = request.user
                    context = {"user": user}
                    return render(request, "assessment/plural.html", context)
            if request.session['password'] != 'valid':
                return render(request, "assessment/plural_password.html", home_context)
            else:
                # session has invalid password
                return render(request, "assessment/plural_password.html", home_context)
        else:
            # set session password as invalid
            request.session['password'] = 'invalid'
            return render(request, "assessment/plural_password.html", home_context)

    if request.method == 'GET':
        if 'password' in request.session:
            if request.session['password'] == 'valid':
                user = request.user
                context = {"user": user}
                return render(request, "assessment/plural.html", context)

    password_form = PluralPasswordForm()
    home_context = {
        "form": password_form
    }
    return render(request, "assessment/plural_password.html", home_context)