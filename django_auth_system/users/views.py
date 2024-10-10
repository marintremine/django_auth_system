from django.shortcuts import render

# Create your views here.
# users/views.py

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    user = request.user
    return render(request, 'users/index.html', {'user': user})

class CustomLoginView(LoginView):
    template_name = 'users/login.html'
    redirect_authenticated_user = True  # Redirige les utilisateurs connectés

    def get_success_url(self):
        return reverse_lazy('home')  # Redirection après succès de la connexion


def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Connexion automatique après l'inscription
            return redirect('home')  # Redirection vers la page d'accueil ou tableau de bord
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')  # Redirection vers la page de connexion après déconnexion



def group_required(group_name):
    def decorator(view_func):
        def wrapper(request, *args, **kwargs):
            if request.user.groups.filter(name=group_name).exists():
                return view_func(request, *args, **kwargs)
            else:
                return render(request, 'users/access_denied.html')
        return wrapper
    return decorator

@login_required
@group_required('artist')
def artist_home(request):
    return render(request, 'users/artist_home.html')

@login_required
@group_required('employee')
def employee_home(request):
    return render(request, 'users/employee_home.html')
