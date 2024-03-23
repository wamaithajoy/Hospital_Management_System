from django.db import models

class VirtualConsultation(models.Model):
    patient_name = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    reason_for_consultation = models.TextField()
    preferred_datetime = models.DateTimeField()

    def __str__(self):
        return f"Consultation for {self.patient_name} on {self.preferred_datetime.strftime('%Y-%m-%d %H:%M')}"
    

class HomeHealthService(models.Model):
    SERVICE_CHOICES = [
        ('Nursing', 'Nursing'),
        ('Therapy', 'Therapy'),
    ]
    
    patient_name = models.CharField(max_length=100)
    contact_information = models.CharField(max_length=100)
    physical_address = models.TextField()
    service_requested = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    medical_history = models.TextField()
    emergency_contact = models.CharField(max_length=100)
    
    def __str__(self):
        return self.patient_name
    
    


class RemoteMonitoring(models.Model):
    PHYSICIAN_CHOICES = [
        ('Dr. Smith', 'Dr. Smith'),
        ('Dr. Johnson', 'Dr. Johnson'),
        ('Dr. Williams', 'Dr. Williams'),
        ('Dr. Brown', 'Dr. Brown'),
        ('Dr. Jones', 'Dr. Jones'),
        ('Dr. Garcia', 'Dr. Garcia'),
        ('Dr. Miller', 'Dr. Miller'),
        ('Dr. Davis', 'Dr. Davis'),
    ]

    patient_name = models.CharField( max_length=100)
    date_of_birth = models.DateField()
    contact_information = models.CharField(max_length=100)
    conditions_to_be_monitored = models.CharField( max_length=100)
    device_preference = models.CharField(max_length=100)
    physician_or_specialist = models.CharField( max_length=100, choices=PHYSICIAN_CHOICES)
    
    
    

