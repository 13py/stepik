from django.shortcuts import render
from django.views import View
from .data import title, description, departures, tours
from .rand import rand


class MainView(View):
    def get(self, request):
        context = {'title': title, 'description': description,
                   'departures': departures, 'tours': {i: tours[i] for i in rand()}}
        return render(request, 'tours/index.html', context)


class DepartureView(View):
    def get(self, request, departure):
        tours_from_city = []
        price = []
        night = []
        for tour in tours.values():
            if departure in tour.values():
                tours_from_city.append(tour)
                price.append(tour['price'])
                night.append(tour['nights'])
        # price = sorted(tours_from_city, key=lambda x: x['price'])
        # night = sorted(tours_from_city, key=lambda x: x['nights'])

        context = {'departures': departures, 'tours': tours, 'title': title,
                   'tours_count': len(tours_from_city), 'price': sorted(price),
                   'night': sorted(night), 'departure': departures[departure]}
        return render(request, 'tours/departure1.html', context)


class TourView(View):
    def get(self, request, id):
        context = {'id': id, 'tours': tours, 'departures': departures, 'title': title}
        return render(request, 'tours/tour.html', context)
