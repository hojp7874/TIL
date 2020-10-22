from django.test import TestCase
from .models import User

# Create your tests here.
class AccountTest(TestCase):
    def setUp(self):
        User.objects.create_user(username='testuser', password='password') # User모델은 암호화가 필요하기 떄문에 .objects.create_user로 하는게 좋다.
        # Setup run before every test method.

    def tearDown(self):
        # Clean up run after every test method.
        pass

    # def test_something_that_will_pass(self):
    #     self.assertFalse(False)

    # def test_something_that_will_fail(self):
    #     self.assertTrue(False)

    # def test_my_first_test(self):
    #     self.assertEquals(1, 2-1)
    #     self.assertNotEquals(1, 2-1)

    def test_user_model_create(self):
        user = User.objects.get(pk=1)
        self.assertEqual(user.username, 'testuser')

    def test_user_str_method(self):
        user = User.objects.get(pk=1)
        self.assertEqual(str(user), 'User object (1)')

    def test_user_phone_field_max_length(self):
        user = User.objects.get(pk=1)
        max_length = user._meta.get_field('phone').max_length
        self.assertEqual(max_length, 11)

    def test_base_templates(self):
        response = self.client.get('/accounts/')
        self.assertContains(response, '<a href="">login</a>') # 로그인 했을때
        self.assertNotContains(response, '<a href="">logout</a>') # 로그인 안했을때
        
        self.client.login(username='testuser', password='password')
        response = self.client.get('/accounts/')
        self.assertContains(response, '<a href="">logout</a>')
        self.assertNotContains(response, '<a href="">login</a>')