from django.urls import path
from users.views import login_request, register, create_profile, show_profile
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', login_request, name='login'),
    path('signup/', register, name='register'),
    path('logout/', LogoutView.as_view(template_name = 'users/logout.html'), name='logout'),
    path('profile/<int:pk>/', show_profile, name='profile'),
    path('create-profile/', create_profile, name='create_profile'),
]