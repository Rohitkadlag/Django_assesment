from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpPatientForm, SignUpDoctorForm
from django.shortcuts import render, redirect
from django.contrib.auth import logout

from .forms import SignUpPatientForm, SignUpDoctorForm
from .models import PatientProfile, DoctorProfile

def home(request):
    return render(request, 'user_auth_app/home.html')

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if hasattr(user, 'patientprofile'):
                return redirect('patient_dashboard')
            elif hasattr(user, 'doctorprofile'):
                return redirect('doctor_dashboard')
    else:
        form = AuthenticationForm()

    return render(request, 'user_auth_app/login.html', {'form': form})







def user_logout(request):
    logout(request)
    return redirect('user_auth_app:home')  # Redirect to the home page





def signup_patient(request):
    if request.method == 'POST':
        form = SignUpPatientForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save the user yet
            user.save()  # Save the user

            patient_profile = PatientProfile.objects.create(
                user=user,
                health_condition=form.cleaned_data['health_condition'],
                address_line1=form.cleaned_data['address_line1'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                pincode=form.cleaned_data['pincode']
            )

            login(request, user)
            return redirect('patient_dashboard')
    else:
        form = SignUpPatientForm()

    return render(request, 'user_auth_app/signup_patient.html', {'form': form})


def signup_doctor(request):
    if request.method == 'POST':
        form = SignUpDoctorForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  # Don't save the user yet
            user.save()  # Save the user

            doctor_profile = DoctorProfile.objects.create(
                user=user,
                speciality=form.cleaned_data['speciality'],
                address_line1=form.cleaned_data['address_line1'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                pincode=form.cleaned_data['pincode']
            )

            login(request, user)
            return redirect('doctor_dashboard')
    else:
        form = SignUpDoctorForm()

    return render(request, 'user_auth_app/signup_doctor.html', {'form': form})
