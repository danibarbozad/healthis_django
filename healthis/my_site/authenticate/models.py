from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(
        blank=False,
        null=False,
        max_length=100
    )
    last_name = models.CharField(
        blank=False,
        null=False,
        max_length=100
    )
    date_of_birth = models.DateField(
        blank=False,
        null=False 
    )
    email = models.CharField(
        blank=False,
        null=False, 
        max_length=100
    )
    phonenumber = models.CharField(
        blank=False,
        null=False,
        max_length=100
    )
    landline_phonenumber = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )    
    zipcode = models.CharField(
        blank=False,
        null=False,
        max_length=100
    )
    neighborhood = models.CharField(
        blank=False,
        null=False,
        max_length=100
    )
    city = models.CharField(
        blank=False,
        null=False,
        max_length=100
    )
    address = models.CharField(
        blank=False,
        null=False,
        max_length=100
    )
    complement = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    state = models.CharField(
        blank=False,
        null=False,
        max_length=100
    )
    objects = models.Manager()
    



class Vacines(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField(
        blank=False,
        null=False,
    )

    vacine = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    dose = models.IntegerField(
        blank=False,
        null=False,
    )

    batch = models.CharField(
        max_length=100,
        blank=False,
        null=False,
    )

    vaccinator = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )

    healthcenter = models.CharField(
        max_length=200,
        blank=False,
        null=False,
    )

    objects = models.Manager()

    



