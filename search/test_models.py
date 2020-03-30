from django.test import TestCase
from django.contrib.auth.models import User
from .models import UserChart, BarChart, LineChart

class UserChartTestCase(TestCase):
    def setUp(self):
        """Set up objects used by all test methods."""
        user = User.objects.create_user(
            username = "test_user1",
            email = "test_user1@test.com",
            password = "test_user1_test"
        )
        UserChart.objects.create(
            user_id = user,
            chart_type = 'bar',
            title = 'This is a test chart title',
            subtitle = 'This is a test chart subtitle'
        )

    def test_user_chart_as_a_string(self):
        """Test the string representation of the object."""
        user = User.objects.get(username="test_user1")
        user_chart = UserChart.objects.get(user_id=user.id)
        expected_object_string = "user_id: " + str(user.id) + \
            " chart_id: " + str(user_chart.id)

        self.assertEqual(str(user_chart), expected_object_string)

class BarChartTestCase(TestCase):
    def setUp(self):
        """Set up objects used by all test methods."""
        user = User.objects.create(
            username = "test_user1",
            email = "test_user1@test.com",
            password = "test_user1_test"
        )
        user_chart = UserChart.objects.create(
            user_id = user,
            chart_type = 'bar',
            title = 'This is a test chart title',
            subtitle = 'This is a test chart subtitle'
        )
        BarChart.objects.create(
            chart_id = user_chart,
            x_data = 'Apple',
            y_data = 10.5
        )

    def test_bar_chart_as_a_string(self):
        """Test the string representation of the object."""
        user = User.objects.get(username="test_user1")
        user_chart = UserChart.objects.get(user_id=user.id)
        bar_chart = BarChart.objects.get(chart_id=user_chart.id)
        expected_object_string = "chart_id: " + str(user_chart.id) + \
            " row_id: " + str(bar_chart.id)   

        self.assertEqual(str(bar_chart), expected_object_string)

class LineChartTestCase(TestCase):
    def setUp(self):
        """Set up objects used by all test methods."""
        user = User.objects.create(
            username = "test_user1",
            email = "test_user1@test.com",
            password = "test_user1_test"
        )
        user_chart = UserChart.objects.create(
            user_id = user,
            chart_type = 'line',
            title = 'This is a test chart title',
            subtitle = 'This is a test chart subtitle'
        )
        LineChart.objects.create(
            chart_id = user_chart,
            date_format = '%m-%d-%Y',
            x_data = '03-30-2020',
            y_data = '10.5'
        )

    def test_line_chart_as_a_string(self):
        """Test the string representation of the object."""
        user = User.objects.get(username="test_user1")
        user_chart = UserChart.objects.get(user_id=user.id)
        line_chart = LineChart.objects.get(chart_id=user_chart.id)
        expected_object_string = "chart_id: " + str(user_chart.id) + \
            " row_id: " + str(line_chart.id)   
            
        self.assertEqual(str(line_chart), expected_object_string)