from django.db import models

# The Booking models here
class booking(models.Model):
 Name = models.CharField(max_length=255)
 No_of_guests = models.DecimalField(max_digits=6, decimal_places=0)
 BookingDate = models.DateTimeField()

 def __str__(self):
  return self.Name

 # The Menutable here
class menu(models.Model):
 Tittle = models.CharField(max_length=255)
 Price = models.DecimalField(max_digits=10, decimal_places=2)
 Inventory = models.DecimalField(max_digits=5, decimal_places=0)

 def __str__(self):
  return f'{self.Tittle} : {str(self.Price)}'