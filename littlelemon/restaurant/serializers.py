from rest_framework import serializers
from .models import menu, booking

# classes here
class menuSerializer(serializers.ModelSerializer):
   class Meta:
      model = menu
      fields = ['Tittle','Price','Inventory']


class bookingSerializer(serializers.ModelSerializer):
   class Meta:
      model = booking
      fields = '__all__'
