# user_auth_app/urls.py
# user_auth_app/urls.py
from django.urls import path
from .views import home, signup_patient, signup_doctor, user_login,user_logout

app_name = 'user_auth_app'

urlpatterns = [
    path('', home, name='home'),
    path('signup/patient/', signup_patient, name='signup_patient'),
    path('signup/doctor/', signup_doctor, name='signup_doctor'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='user_logout'),
    # Add other URL patterns as needed
]
