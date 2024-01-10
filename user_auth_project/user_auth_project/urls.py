from django.contrib import admin
from django.urls import path, include
from user_auth_app.views import user_login
from dashboard_app.views import patient_dashboard, doctor_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', user_login, name='login'),
    path('dashboard/patient/', patient_dashboard, name='patient_dashboard'),
    path('dashboard/doctor/', doctor_dashboard, name='doctor_dashboard'),
    path('', include('user_auth_app.urls')),  # Include only once for the root path
    # Other URL patterns...
]
