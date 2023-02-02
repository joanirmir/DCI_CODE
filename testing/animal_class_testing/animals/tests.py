from django.test import TestCase

# Create your tests here.
from .models import Animal



class AnimalTestCase(TestCase):
    def setUp(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")

    def test_animals_can_speak(self):
        # fetching a lion
        lion = Animal.objects.get(name='lion')
        self.assertEqual(lion.speak(), "The lion says \"roar\"")