from django.test import TestCase
from django.shortcuts import reverse

class CreateChartViewTestCase(TestCase):

   def test_correct_template_is_used(self):
        """Test correct template is used."""
        response = self.client.get(reverse('barchart:create_chart'))

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'barchart/chart.html')

class ViewChartViewTestCase(TestCase):

   def test_correct_template_is_used(self):
        """Test correct template is used."""
        response = self.client.get('/barchart/1/view/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'barchart/viewchart.html')