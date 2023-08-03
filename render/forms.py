# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django import forms
from .models import Patient
from django.forms import ModelForm


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'room_number', 'age', 'sex', 'doctor', 'reason_adm', 'notes', 'pub_date','body_temp', 'pulse_rate', 'respiration_rate', 'systolic','diastolic',)
        labels = {
            'first_name': 'First Name',
            'last_name': 'Last Name',
            'room_number': 'Room Number',
            'age': 'Age',
            'sex': 'Sex',
            'doctor': 'Doctor',
            'reason_adm': 'Reason Admitted',
            'notes': 'Notes',
            'pub_date': 'Date Admitted',
            'body_temp': 'Body Temperature',
            'pulse_rate': 'Pulse Rate',
            'respiration_rate': 'Respiration Rate',
            'Systolic': 'Blood Pressure (Systolic)',
            'Diastolic': 'Blood Pressure (Diastolic)',
        }
        widgets = {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'room_number': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Room Number'}),
            'age': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Age'}),
            'sex': forms.Select(attrs={'class':'form-control', 'placeholder':'Sex'}),
            'doctor': forms.Select(attrs={'class':'form-control', 'placeholder':'Doctor'}),
            'reason_adm': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Reason Admitted'}),
            'notes': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Notes'}),
            'pub_date': forms.SelectDateWidget(attrs={'class':'form-control', 'placeholder':'Date Admitted'}),
            'body_temp': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Body Temperature'}),
            'pulse_rate': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Pulse Rate'}),
            'respiration_rate': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Respiration Rate'}),
            'systolic': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Blood Pressure (Systolic)'}),
            'diastolic': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Blood Pressure (Diastolic)'}),

        }

# class VitalForm(ModelForm):
#     class Meta:
#         model = Vital
#         fields = ('patient','body_temp', 'pulse_rate', 'respiration_rate', 'blood_pressure',)
#         labels = {
#             'patient':'Patient',
#             'body_temp': 'Body Temperature',
#             'pulse_rate': 'Pulse Rate',
#             'respiration_rate': 'Respiration Rate',
#             'blood_pressure': 'Blood Pressure',
#         }
#         widgets = {
#             'patient': forms.Select(attrs={'class':'form-control', 'placeholder':'Patient'}),
#             'body_temp': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Body Temperature'}),
#             'pulse_rate': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Pulse Rate'}),
#             'respiration_rate': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Respiration Rate'}),
#             'blood_pressure': forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Blood Pressure'}),
#         }
