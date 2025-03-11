from django.http import HttpResponse, HttpResponseNotFound

def handler404(request, exception):
    return HttpResponse("Where is the fucking page ? XD")
