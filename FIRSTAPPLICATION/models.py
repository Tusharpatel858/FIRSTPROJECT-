from django.db import models

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=150)
    Person_id = models.AutoField(primary_key=True)
    Person_contact_No = models.CharField(max_length=10)
    Person_address= models.CharField(max_length=150)

    def __str__(self):
        return self.first_name