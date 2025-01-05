from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator



# Create your models here.
class sellerRegister(models.Model):
    ACCOUNT_TYPE = {
        "B": "Business",
        "C": "Customer",
    }
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    contact = models.IntegerField(unique=True,validators=[ MinValueValidator(0),  MaxValueValidator(9999999999)])
    password = models.CharField(max_length=200)
    accountType = models.CharField(max_length=1, choices=ACCOUNT_TYPE, default='B')

    companyName = models.CharField(max_length=100)
    storeName = models.CharField(max_length=100)
    category = models.CharField(max_length=1, choices=ACCOUNT_TYPE, default='B')
    address = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class countryCodes(models.Model):
    country = models.CharField(max_length=100)
    dialCode = models.CharField(max_length=10)
    image = models.CharField(max_length=100)
    def __str__(self):
        return self.country

# <div class="px-4 py-2 flex">
#     <input type="text" id="searchInput" class="w-full px-4 py-2 text-sm border-dark-600 border-b-4 bg-gray-800 text-gray-200" placeholder="Search country...">
# </div>