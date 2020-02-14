from django.test import TestCase
from .forms import UserLoginForm

# Create your tests here.
class UserLoginForm_Test(TestCase):

    def test_str(self):
        test_username = UserLoginForm(username= "A username")
        self.assertEqual(str(test_username), "A username")

    
