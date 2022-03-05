from django.shortcuts import render
from django.views.generic.list import ListView
from users.forms import UserCreateForm, UserUpdateForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin

from users.models import ArikeUser

def login_view(request):
    return render(request, "login.html")

class AuthorisedUserManager(LoginRequiredMixin):
    def get_queryset(self):
        return ArikeUser.objects.all()
class GenericUserListView(ListView):
    model: ArikeUser
    context_object_name = 'users'
    queryset = ArikeUser.objects.all()
    template_name = 'user/user_list.html'

class GenericUserCreateView(CreateView):
    form_class = UserCreateForm
    template_name = 'user/user_create.html'
    success_url = "/dashboard"
    
class GenericUserUpdateView(AuthorisedUserManager, UpdateView):
    form_class = UserUpdateForm
    template_name = 'user/user_update.html'
    success_url = "/dashboard"

class GenericUserDetailView(DetailView):
    model = ArikeUser
    template_name = 'user/user_detail.html'

class GenericUserDeleteView(DeleteView):
    model = ArikeUser
    template_name = 'user/user_delete.html'
    success_url = "/dashboard"
