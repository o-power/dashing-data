def uploaded_data_function(request):
    """
    Function to add chart_data to the template context.
    """
    chart_title = request.session.get('chart_title', '')
    chart_subtitle = request.session.get('chart_subtitle', '')
    date_format = request.session.get('date_format', '')
    chart_data = request.session.get('chart_data', [])

    return {'chart_title': chart_title,
            'chart_subtitle': chart_subtitle,
            'date_format': date_format,
            'chart_data': chart_data}