from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from accounts.forms import RegisterForm, ProfileForm


class RegistrationView(CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('index')
    template_name = 'djano_registration/registration_form.html'

class ProfileView(UpdateView):
    form_class = ProfileForm
    success_url = reverse_lazy('profile')
    template_name = 'accounts/profile.html'


    def get(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return redirect('login')
        return super().get(request, *args, **kwargs)

    def get_object(self, queryset = None):
        return self.request.user

