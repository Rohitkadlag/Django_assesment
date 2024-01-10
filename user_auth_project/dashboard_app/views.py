# views.py in dashboard_app

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from user_auth_app.models import PatientProfile, DoctorProfile

@login_required
def patient_dashboard(request):
    patient_profile = request.user.patientprofile
    return render(request, 'dashboard_app/patient_dashboard.html', {'patient_profile': patient_profile})

@login_required
def doctor_dashboard(request):
    doctor_profile = request.user.doctorprofile
    return render(request, 'dashboard_app/doctor_dashboard.html', {'doctor_profile': doctor_profile})
