from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from myapp.forms import BookingForm

# Create your views here.

# CREATING FORMS ***************
# from myapp.forms import InputForm

def form_view(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {"form": form}
    return render(request, "booking.html", context)



# ROUTING*******************

# def home(request):
#     return HttpResponseNotFound("Welcome to Little Lemon!")

# def about(request):
#     return HttpResponse("About us")

# def menu(request):
#     return HttpResponse("Menu")

# def book(request):
#     return HttpResponse('Make a booking')



# def home(request):
#     path = request.path
#     scheme = request.scheme
#     method = request.method
#     address = request.META['REMOTE_ADDR']

#     msg = f"""<br>
#         <br>Path: {path}
#         <br>Address: {address}
#         <br>Scheme: {scheme}
#         <br>Method: {method}
#         response = HttpResponse("This work")
#         return response
#     """
#     return HttpResponse(msg, content_type='text/html', charset='utf-8')

#MODELS CRUD**************

# def menuitems(request, dish):
#     items = {
#         'pasta': 'Pasta is a type of noodle',
#         'falafel': 'Falafel are deep fried',
#         'cheesecake': 'Is a type of dessert',
#     }

#     description = items [dish]

#     return HttpResponse(f"<h2> {dish} </h2>" + description)

# def drinks(request, drink_name):
#     drink = {
#         'mocha': 'type of coffee',
#         'tea': 'type of beverage',
#         'lemonade': 'type of refreshment',
#         'vermutinho': 'With olives and orange'
#     }

#     choice_of_drink = drink[drink_name]

#     return HttpResponse(f"<h2> {drink_name} </h2>" + choice_of_drink)
