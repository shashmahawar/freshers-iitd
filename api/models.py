from django.db import models

# Create your models here.

class KerberosData(models.Model):
    kerberos = models.CharField(max_length=9, unique=True)
    name = models.CharField(max_length=255)
    hostel = models.CharField(max_length=100)

    def __str__(self):
        return self.kerberos

class registrationToken(models.Model):
    kerberos = models.CharField(max_length=9, unique=True)
    token = models.CharField(max_length=255)

    def __str__(self):
        return self.kerberos

class forgotToken(models.Model):
    kerberos = models.CharField(max_length=9, unique=True)
    token = models.CharField(max_length=255)

    def __str__(self):
        return self.kerberos