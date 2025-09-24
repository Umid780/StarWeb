from django.shortcuts import render, get_object_or_404
from .models import Car

def car_list(request):
    q = request.GET.get('q','')
    cars = Car.objects.all()
    if q:
        cars = cars.filter(title__icontains=q)  # oddiy qidiruv
    return render(request, 'cars/list.html', {'cars': cars, 'q': q})

def car_detail(request, pk):
    car = get_object_or_404(Car, pk=pk)
    return render(request, 'cars/detail.html', {'car': car})