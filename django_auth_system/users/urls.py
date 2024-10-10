from django.contrib.auth.views import LogoutView
from django.urls import path

from users.views import CustomLoginView, artist_home, employee_home, signup_view, home, logout_view


urlpatterns = [
    path('', home, name='home'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('signup/', signup_view, name='signup'),
    path('logout/', logout_view, name='logout'),
    path('artist/', artist_home, name='artist_home'),
    path('employee/', employee_home, name='employee_home'),
]