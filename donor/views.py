from django.shortcuts import render, redirect
from .models import Donor, BloodRequest

def home(request):
    return render(request, 'home.html')

def add_donor(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        blood_group = request.POST['blood_group']
        phone = request.POST['phone']
        location = request.POST['location']

        Donor.objects.create(
            name=name,
            age=age,
            blood_group=blood_group,
            phone=phone,
            location=location
        )
        return redirect('view_donors')

    return render(request, 'add_donor.html')


def view_donors(request):
    donors = Donor.objects.all()
    return render(request, 'view_donors.html', {'donors': donors})


def search_donor(request):
    donors = []
    if request.method == 'POST':
        bg = request.POST['blood_group']
        donors = Donor.objects.filter(blood_group=bg)

    return render(request, 'search.html', {'donors': donors})


def request_blood(request):
    if request.method == 'POST':
        patient_name = request.POST['patient_name']
        blood_group = request.POST['blood_group']
        location = request.POST['location']

        BloodRequest.objects.create(
            patient_name=patient_name,
            blood_group=blood_group,
            location=location
        )
        return redirect('home')

    return render(request, 'request.html')