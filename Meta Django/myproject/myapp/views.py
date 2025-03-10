from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home(request):
    path = request.path
    scheme = request.scheme
    method = request.method
    address = request.META['REMOTE_ADDR']

    msg = f"""<br>
        <br>Path: {path}
        <br>Address: {address}
        <br>Scheme: {scheme}
        <br>Method: {method}
        response = HttpResponse("This work")
        return response
    """
    return HttpResponse(msg, content_type='text/html', charset='utf-8')
