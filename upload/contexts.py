def uploaded_data_function(request):
    """
    
    """
    uploaded_data = request.session.get('uploaded_data', {})

    if bool(uploaded_data):
        print('Hello 1')
        x_data = uploaded_data['x_data']
        y_data = uploaded_data['y_data']
    else:
        print('Hello 2')
        x_data = []
        y_data = []
        

    return {'x_data': x_data, 'y_data': y_data}