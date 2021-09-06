from django.db import models

# Create your models here.+

class contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=250)
    phone=models.CharField(max_length=10)
    status=models.BooleanField(default=True)
    def __str__(self):
        return self.name
