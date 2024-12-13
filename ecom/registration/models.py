from django.db import models

# Create your models here.
class register(models.Model):
    ACCOUNT_TYPE = {
        "B": "Business",
        "C": "Customer",
    }
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=500)
    accountType = models.CharField(max_length=1, choices=ACCOUNT_TYPE, default='C')

    def __str__(self):
        return self.name