# dashboard_app/urls.py

from django.urls import path
from .views import patient_dashboard, doctor_dashboard

app_name = 'dashboard_app'

urlpatterns = [
    path('patient/', patient_dashboard, name='patient_dashboard'),
    path('doctor/', doctor_dashboard, name='doctor_dashboard'),
    # Add other URL patterns as needed
]
