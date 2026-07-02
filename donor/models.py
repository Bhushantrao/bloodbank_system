from django.db import models

class Donor(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    blood_group = models.CharField(max_length=5)
    phone = models.CharField(max_length=15)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class BloodRequest(models.Model):
    patient_name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=5)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Pending')

    def __str__(self):
        return self.patient_name