from django.test import TestCase
from restaurant.models import menu

# test class here
class MenuTest(TestCase):
 def test_get_item(self):
  item = menu.objects.create(Tittle="Rice", Price=200, Inventory=20)
  itemstr = item.get_item()
  self.assertEqual(itemstr, 'Rice : 200')