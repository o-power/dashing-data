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
                                'date_format': '%m-%d-%Y',
                                'x_data': 'Apple\nBanana\nOrange',
                                'y_data': '10\nBanana\n7'
                            })
        
        self.assertFalse(upload_data_form.is_valid())
        self.assertEqual(upload_data_form.errors['y_data'], ['y data must be numeric.'])
    
    def test_form_validation_fails_if_xy_mismatch(self):
        """
        Test form validation fails if the number of
        y values does not match the x values.
        """
        upload_data_form = UploadDataForm({
                                'chart_title': 'This is the title',
                                'chart_subtitle': 'This is a subtitle',
                                'date_format': '%m-%d-%Y',
                                'x_data': 'Apple\nBanana\nOrange',
                                # y_data only has 2 entries
                                'y_data': '10\n5.5'
                            })

        self.assertFalse(upload_data_form.is_valid())

    def test_form_validation_fails_for_nondate_x_data(self):
        """
        Test form validation fails if the x data
        contains data which is not a date.
        """
        upload_data_form = UploadDataForm({
                                'chart_title': 'This is the title',
                                'chart_subtitle': 'This is a subtitle',
                                'date_format': '%m-%d-%Y',
                                # non-date value in x_data
                                'x_data': '03-30-2020\nBanana\n04-01-2020',
                                'y_data': '10\n5.5\n7'
                            })

        self.assertFalse(upload_data_form.is_valid())
    
    def test_form_validation_fails_for_incorrectformat_x_data(self):
        """
        Test form validation fails if the x data
        contains a date in the incorrect format.
        """
        upload_data_form = UploadDataForm({
                                'chart_title': 'This is the title',
                                'chart_subtitle': 'This is a subtitle',
                                'date_format': '%m-%d-%Y',
                                # x_data with an incorrect date format
                                'x_data': '2020-03-30\n2020-03-31\n2020-01-04',
                                'y_data': '10\n5.5\n7'
                            })

        self.assertFalse(upload_data_form.is_valid())

