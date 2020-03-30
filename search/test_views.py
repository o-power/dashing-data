from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserChart
from django.shortcuts import reverse

class AllChartsViewTestCase(TestCase):
    def setUp(self):
        """Set up objects used by all test methods."""
        # a user with 2 charts
        user = User.objects.create_user(
            username = 'test_user1',
            email = 'test_user1@test.com',
            password = 'test_user1_test'
        )
        UserChart.objects.create(
            user_id = user,
            chart_type = 'bar',
            title = 'This is a test chart title 1',
            subtitle = 'This is a test chart subtitle 1'
        )
        UserChart.objects.create(
            user_id = user,
            chart_type = 'bar',
            title = 'This is a test chart title 2',
            subtitle = 'This is a test chart subtitle 2'
        )

        # a user with 1 chart
        user = User.objects.create_user(
            username = 'test_user2',
            email = 'test_user2@test.com',
            password = 'test_user2_test'
        )
        UserChart.objects.create(
            user_id = user,
            chart_type = 'bar',
            title = 'This is a test chart title 3',
            subtitle = 'This is a test chart subtitle 3'
        )

    def test_redirect_if_not_logged_in(self):
        """Test user is redirected to login if not logged in."""
        response = self.client.get(reverse('search:all_charts'))

        self.assertRedirects(response, '/accounts/login/?next=/search/charts/')

    def test_correct_template_is_used(self):
        """Test correct template is used."""
        login = self.client.login(username='test_user1', password='test_user1_test')
        response = self.client.get(reverse('search:all_charts'))

        self.assertEqual(response.context['user'].username, 'test_user1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'search/savedcharts.html')

    def test_context_contains_users_charts(self):
        """
        Test the context dictionary contains a
        charts item containing the user's charts.
        """
        login = self.client.login(username='test_user1', password='test_user1_test')
        response = self.client.get(reverse('search:all_charts'))

        user = User.objects.get(username="test_user1")
        charts = UserChart.objects.filter(user_id=user.id)

        self.assertEqual(response.context['user'].username, 'test_user1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['charts']), len(charts))

class DoSearchViewTestCase(TestCase):
    def setUp(self):
        """Set up objects used by all test methods."""
        # a user with 2 charts
        user = User.objects.create_user(
            username = 'test_user1',
            email = 'test_user1@test.com',
            password = 'test_user1_test'
        )
        UserChart.objects.create(
            user_id = user,
            chart_type = 'bar',
            title = 'This is a chart showing apples 1',
            subtitle = 'This is a test chart subtitle 1'
        )
        UserChart.objects.create(
            user_id = user,
            chart_type = 'bar',
            title = 'This is a chart showing apples 2',
            subtitle = 'This is a test chart subtitle 2'
        )
        UserChart.objects.create(
            user_id = user,
            chart_type = 'bar',
            title = 'This is a chart showing bananas 2',
            subtitle = 'This is a test chart subtitle 2'
        )

        # a user with 1 chart
        user = User.objects.create_user(
            username = 'test_user2',
            email = 'test_user2@test.com',
            password = 'test_user2_test'
        )
        UserChart.objects.create(
            user_id = user,
            chart_type = 'bar',
            title = 'This is a chart showing apples 3',
            subtitle = 'This is a test chart subtitle 3'
        )    

    def test_redirect_if_not_logged_in(self):
        """Test user is redirected to login if not logged in."""
        response = self.client.get(reverse('search:do_search'))
        
        self.assertRedirects(response, '/accounts/login/?next=/search/result/')

    def test_correct_template_is_used(self):
        """Test correct template is used."""
        login = self.client.login(username='test_user1', password='test_user1_test')
        response = self.client.get('/search/result/?q=apples')
        
        self.assertEqual(response.context['user'].username, 'test_user1')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'search/savedcharts.html')
    
    def test_search_returns_correct_results(self):
        """Test correct template is used."""
        login = self.client.login(username='test_user1', password='test_user1_test')
        response = self.client.get('/search/result/?q=apples')
        
        user = User.objects.get(username="test_user1")
        charts = UserChart.objects.filter(user_id=user.id,title__icontains='apples')
        
        self.assertEqual(response.context['user'].username, 'test_user1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['charts']), len(charts))