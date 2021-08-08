from django.forms import ModelForm
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _

from .models import Company

# class CompanyCreationForm(forms.CompanyCreationForm):

#     error_message = forms.UserCreationForm.error_messages.update(
#         {"duplicate_username": _("This username has already been taken.")}
#     )

#     class Meta(forms.UserCreationForm.Meta):
#         model = User

#     def clean_username(self):
#         username = self.cleaned_data["username"]

#         try:
#             User.objects.get(username=username)
#         except User.DoesNotExist:
#             return username

#         raise ValidationError(self.error_messages["duplicate_username"])

class CompanyCreationForm(ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'logo', 'website']
