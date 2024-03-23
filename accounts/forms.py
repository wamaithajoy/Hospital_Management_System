from django import forms
from .models import VirtualConsultation
from .models import HomeHealthService    
from .models import RemoteMonitoring

class VirtualConsultationForm(forms.ModelForm):
    class Meta:
        model = VirtualConsultation
        fields = [
            'patient_name', 'date_of_birth', 'phone_number', 'email',
            'reason_for_consultation', 'preferred_datetime',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'preferred_datetime': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'consent_to_terms': forms.CheckboxInput()
        }
        

class HomeHealthServiceForm(forms.ModelForm):
    class Meta:
        model = HomeHealthService
        fields = ['patient_name', 'contact_information', 'physical_address',
                  'service_requested', 'medical_history', 'emergency_contact']
        widgets = {
            'consent': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            
        }


class RemoteMonitoringForm(forms.ModelForm):
    class Meta:
        model = RemoteMonitoring
        fields = [
            'patient_name', 'date_of_birth', 'contact_information', 'conditions_to_be_monitored',
            'device_preference', 'physician_or_specialist'
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'consent_to_data_collection': forms.CheckboxInput()
        }

        
        
