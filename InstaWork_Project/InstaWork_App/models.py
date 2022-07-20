from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.urls import reverse
from django.core.validators import RegexValidator

class User(models.Model):
    firstName = models.CharField(max_length=50,null=False)
    lastName = models.CharField(max_length=50,null=False)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    # phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True) # validators should be a list
    phoneNo = models.CharField(validators=[phone_regex], max_length=17)
    emailID = models.CharField(max_length=50)
    role = models.CharField(max_length=10, null=False, default="regular")
    
    def __str__(self):
        return self.firstName +" "+ self.lastName

    def get_absolute_url(self):
        return reverse("InstaWork_App-home", kwargs={"pk": self.pk})
    