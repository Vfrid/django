import datetime
from django.contrib.auth.models import User

from django.db import models
from django.utils import timezone
    
# class Doctor(models.Model):
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField('Doctor Email')

#     def __str__(self):
#         return self.first_name + ' ' + self.last_name
    

SEX_OPTIONS = (
    ("MALE", "Male"),
    ("FEMALE", "Female"),
)

class Patient(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    room_number = models.IntegerField()
    age = models.PositiveIntegerField(null=True, blank=False)
    sex = models.CharField(max_length=6, choices=SEX_OPTIONS,null=True, blank=False)
    doctor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    reason_adm = models.CharField(max_length=500)
    notes = models.CharField(max_length=1000)
    body_temp = models.IntegerField(null=True, blank=False)
    pulse_rate = models.IntegerField(null=True, blank=False)
    respiration_rate = models.IntegerField(null=True, blank=False)
    systolic = models.IntegerField(null=True, blank=False)
    diastolic = models.IntegerField(null=True, blank=False)

    pulse_eval = "failure pulse"
    resp_eval = "failure respiratory"
    systolic_eval = "failure systolic"
    diastolic_eval = "failure diastolic"

    def pulseEvaluation(self,pulse,age):
        if int(age) < 2:
            if int(pulse) > 160:
                return "High"
            elif int(pulse) > 80:
                return "Normal"
            else:
                return "Low"

        elif int(age) < 4:
            if int(pulse) > 130:
                return "High"
            elif int(pulse) > 80:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 6:
            if int(pulse) > 120:
                return "High"
            elif int(pulse) > 80:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 13:
            if int(pulse) > 110:
                return "High"
            elif int(pulse) > 75:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 19:
            if int(pulse) > 90:
                return "High"
            elif int(pulse) > 60:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 70:
            if int(pulse) > 100:
                return "High"
            elif int(pulse) > 60:
                return "Normal"
            else:
                return "Low"
            
        if int(age) > 69:
            if int(pulse) > 100:
                return "High"
            elif int(pulse) > 60:
                return "Normal"
            else:
                return "Low"
            
    def respEvaluation(self,respiration_rate,age):
        if int(age) < 2:
            if int(respiration_rate) > 60:
                return "High"
            elif int(respiration_rate) > 30:
                return "Normal"
            else:
                return "Low"

        elif int(age) < 4:
            if int(respiration_rate) > 40:
                return "High"
            elif int(respiration_rate) > 24:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 6:
            if int(respiration_rate) > 34:
                return "High"
            elif int(respiration_rate) > 22:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 13:
            if int(respiration_rate) > 30:
                return "High"
            elif int(respiration_rate) > 18:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 19:
            if int(respiration_rate) > 20:
                return "High"
            elif int(respiration_rate) > 12:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 70:
            if int(respiration_rate) > 20:
                return "High"
            elif int(respiration_rate) > 12:
                return "Normal"
            else:
                return "Low"
        
        if int(age) > 69:
            if int(respiration_rate) > 20:
                return "High"
            elif int(respiration_rate) > 12:
                return "Normal"
            else:
                return "Low"
    
    def tempEvaluation(self,body_temp,age):
        if int(age) < 2:
            if int(body_temp) > 100:
                return "High"
            elif int(body_temp) > 98:
                return "Normal"
            else:
                return "Low"

        elif int(age) < 4:
            if int(body_temp) > 100:
                return "High"
            elif int(body_temp) > 98:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 6:
            if int(body_temp) > 100:
                return "High"
            elif int(body_temp) > 97:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 13:
            if int(body_temp) > 99:
                return "High"
            elif int(body_temp) > 97:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 19:
            if int(body_temp) > 100:
                return "High"
            elif int(body_temp) > 96:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 70:
            if int(body_temp) > 100:
                return "High"
            elif int(body_temp) > 96:
                return "Normal"
            else:
                return "Low"
        
        if int(age) > 69:
            if int(body_temp) > 100:
                return "High"
            elif int(body_temp) > 96:
                return "Normal"
            else:
                return "Low"
            
    def systolicEvaluation(self,systolic,age):
        if int(age) < 2:
            if int(systolic) > 101:
                return "High"
            elif int(systolic) > 73:
                return "Normal"
            else:
                return "Low"

        elif int(age) < 4:
            if int(systolic) > 113:
                return "High"
            elif int(systolic) > 79:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 6:
            if int(systolic) > 111:
                return "High"
            elif int(systolic) > 81:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 13:
            if int(systolic) > 121:
                return "High"
            elif int(systolic) > 83:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 19:
            if int(systolic) > 121:
                return "High"
            elif int(systolic) > 93:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 70:
            if int(systolic) > 121:
                return "High"
            elif int(systolic) > 89:
                return "Normal"
            else:
                return "Low"
        
        if int(age) > 69:
            if int(systolic) > 120:
                return "High"
            elif int(systolic) > 89:
                return "Normal"
            else:
                return "Low"
    
    def diastolicEvaluation(self,diastolic,age):
        if int(age) < 2:
            if int(diastolic) > 71:
                return "High"
            elif int(diastolic) > 49:
                return "Normal"
            else:
                return "Low"

        elif int(age) < 4:
            if int(diastolic) > 81:
                return "High"
            elif int(diastolic) > 49:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 6:
            if int(diastolic) > 79:
                return "High"
            elif int(diastolic) > 49:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 13:
            if int(diastolic) > 81:
                return "High"
            elif int(diastolic) > 53:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 19:
            if int(diastolic) > 81:
                return "High"
            elif int(diastolic) > 61:
                return "Normal"
            else:
                return "Low"
            
        if int(age) < 70:
            if int(diastolic) > 81:
                return "High"
            elif int(diastolic) > 59:
                return "Normal"
            else:
                return "Low"
        
        if int(age) > 69:
            if int(diastolic) > 81:
                return "High"
            elif int(diastolic) > 59:
                return "Normal"
            else:
                return "Low"
   
    pub_date = models.DateTimeField("date published")
    def __str__(self):
        return f"{self.first_name + ' ' + self.last_name}"
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now