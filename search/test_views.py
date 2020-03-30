from django.test import TestCase
from django.contrib.auth.models import User
from django.shortcuts import reverse

#class LogInTest(TestCase):
#    def setUp(self):
#        self.credentials = {
#            'username': 'testuser',
#            'password': 'secret'}
#        User.objects.create_user(**self.credentials)
#    def test_login(self):
#        # send login data
#        response = self.client.post('/login/', self.credentials, follow=True)
#        # should be logged in now
#        self.assertTrue(response.context['user'].is_active)

class AllChartsViewTestCase(TestCase):
    def setUp(self):
        """Set up objects used by all test methods."""
        user = User.objects.create(
            username = 'test_user1',
            email = 'test_user1@test.com',
            password = 'test_user1_test'
        )

    def test_redirect_if_not_logged_in(self):
        response = self.client.get(reverse('search:all_charts'))
        self.assertRedirects(response, '/accounts/login/?next=/search/charts/')

    # def test_all_charts_view(self):
    #     user = User.objects.get(username='test_user1')
    #     response = self.client.post('/accounts/login/',
    #         {'username': user.username, 'password': user.password}
    #         , follow=True)
    #     response = self.client.get('/search/charts/')
    #     print(response)
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'search/savedcharts.html')