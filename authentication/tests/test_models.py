from rest_framework.test import APITestCase
from authentication.models import CustomUser


class TestModel(APITestCase):
    
    def test_creates_user(self):
        user = CustomUser.objects.create_user('ahmad', 'ahmad@admin.com', 'Qwerty')
        self.assertIsInstance(user, CustomUser)
        self.assertFalse(user.is_staff)
        self.assertEqual(user.email, 'ahmad@admin.com')
        
    def test_raises_error_when_no_username(self):
        self.assertRaises(ValueError, CustomUser.objects.create_user, username="", email='ahmad@admin.com', password='Qwerty')
        self.assertRaisesMessage(ValueError, "The username must be set, do not forget")
    
