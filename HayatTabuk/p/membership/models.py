from django.db import models

# Create your models here.

class Membership(models.Model):
    Fname=models.CharField(max_length=250)
    Lname=models.CharField(max_length=250)
    telephone=models.CharField(max_length=10)
    subject=[
        
        ("1M", "One Month"),
        ("2M", "2 Month"),
        ("Iron", "Iron Equipment"),
        ("Swim", "swimming pool")
        
        ]
    message=models.CharField(max_length=600)

    def __str__(self):
        return self.Fname