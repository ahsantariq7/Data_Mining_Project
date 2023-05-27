def handle_uploaded_file(f):  
    with open('create_output/static'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk) 