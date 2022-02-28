from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class AdminStaffRequiredMixin(LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff
