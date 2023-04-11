from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class VolunteerUser(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    volunteername = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    passcode = models.CharField(max_length=200)
    choice=(("1","medical"),("2","food"),("3","scribe"),("4","others"))
    Areaofinterest=models.CharField(max_length=50,choices=choice,default="1")
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)