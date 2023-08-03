from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.contrib import messages
from .models import  Patient
from .forms import PatientForm

class HomeView(generic.ListView):
    template_name = "render/home.html"
    context_object_name = "latest_question_list"
    def get_queryset(self):
        return Patient.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")
    
def patient_list(request):
    if request.user.is_authenticated:
        me = request.user.id
        patients = Patient.objects.filter(doctor= me)

        for patient in patients:
            patient.pulse_eval = patient.pulseEvaluation(patient.pulse_rate, patient.age)
            patient.resp_eval = patient.respEvaluation(patient.respiration_rate, patient.age)
            patient.temp_eval = patient.tempEvaluation(patient.body_temp, patient.age)
            patient.systolic_eval = patient.systolicEvaluation(patient.systolic, patient.age)
            patient.diastolic_eval = patient.diastolicEvaluation(patient.diastolic, patient.age)

        # vitals = Vital.objects.filter(patient=patients)
        return render(request, 'render/patient_list.html',{
            "patients":patients,
            # "vitals": vitals,
        })
    else:
        messages.success(request,('You are not permitted to view this page until you are logged in.'))
        return redirect('home')

def add_patient(request):
    if request.user.is_authenticated:
        submitted=False
        if request.method == "POST":
            form = PatientForm(request.POST)
            if form.is_valid:
                form.save()
            # return HttpResponseRedirect('/add_patient?submitted=True')
                return redirect('patient_list')
        else:
            form = PatientForm
            if 'submitted' in request.GET:
                submitted = True
        return render(request, 'render/add_patient.html', {
            "form":form,
            "submitted":submitted,
            })
    else:
        messages.success(request,('You are not permitted to view this page until you are logged in.'))
        return redirect('home')
    

# def add_vital(request):
#     submitted=False
#     if request.method == "POST":
#         form = VitalForm(request.POST)
#         if form.is_valid:
#             form.save()
#             # return HttpResponseRedirect('/add_patient?submitted=True')
#             return redirect('patient_list')
#     else:
#         form = VitalForm
#         if 'submitted' in request.GET:
#             submitted = True
#     return render(request, 'render/add_vital.html', {
#         "form":form,
#         "submitted":submitted,
#     })
def update_patient(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    form = PatientForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        return redirect('patient_list')
    return render(request, 'render/update_patient.html', {
        "patient":patient,
        "form":form,
    })