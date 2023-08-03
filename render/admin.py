from django.contrib import admin

from .models import  Patient

# class VitalsInline(admin.TabularInline):
#     model = Vital
#     extra = 1


class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["first_name", "last_name"]}),
        ("Date Admitted", {"fields": ["pub_date"],}),
        ("Patient Information", {"fields": ["room_number", "age", "sex", "doctor", "reason_adm", "notes"]}),
        ("Vitals", {"fields": ["body_temp", "pulse_rate", "respiration_rate", "blood_pressure"]}),
    ]
    # inlines = [VitalsInline]
    list_display = ["first_name", "last_name","room_number", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["first_name", "last_name", "room_number"]

# class DoctorAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {"fields": ["first_name", "last_name"]}),
#         (None, {"fields": ["email"]})
#     ]
#     list_display = ["first_name", "last_name",]
#     search_fields = ["first_name", "last_name"]

admin.site.register(Patient, PatientAdmin,)
# admin.site.register(Doctor, DoctorAdmin)