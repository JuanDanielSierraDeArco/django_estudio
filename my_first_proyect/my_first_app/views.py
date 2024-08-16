from django.shortcuts import render

# Create your views here.
def my_view(request):
    car_list = [
    {"title": "BMW"},
    {"title": "Mazda"},
    {"title": "Toyota"},
    {"title": "Honda"},
    {"title": "Ford"},
    {"title": "Chevrolet"},
    {"title": "Audi"},
    {"title": "Mercedes-Benz"},
    {"title": "Nissan"},
    {"title": "Hyundai"}]

    context = {"car_list": car_list}

    return render(request, "my_first_app/car_list.html", context)