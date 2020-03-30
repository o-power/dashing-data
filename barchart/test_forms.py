from django.test import TestCase
from .forms import UploadDataForm

class UploadDataFormTestCase(TestCase):

    def test_correct_message_for_nonnumeric_y_data(self):
        """
        Test correct error message is displayed when
        non-numeric y data is entered
        """
        upload_data_form = UploadDataForm({
                                'chart_title': 'This is the title',
                                'chart_subtitle': 'This is a subtitle',
                                'x_data': 'Apple\nBanana\nOrange',
                                'y_data': '10\nBanana\n7'
                            })
        
        self.assertFalse(upload_data_form.is_valid())
        self.assertEqual(upload_data_form.errors['y_data'], ['y data must be numeric.'])
    
    def test_form_validation_fails_if_xy_mistmatch(self):
        """
        Test form validation fails if the number of
        y values does not match the x values.
        """
        upload_data_form = UploadDataForm({
                                'chart_title': 'This is the title',
                                'chart_subtitle': 'This is a subtitle',
                                'x_data': 'Apple\nBanana\nOrange',
                                'y_data': '10\n5.5'
                            })

        self.assertFalse(upload_data_form.is_valid())