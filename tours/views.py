from django.http import Http404
from django.shortcuts import render
from django.views import View

from .data import title, description, departures, tours
from .rand import rand
from .tours_from_city_date import tours_city_dates


class MainView(View):
    def get(self, request):
        context = {'title': title, 'description': description,
                   'departures': departures, 'tours': {i: tours[i] for i in rand()}}
        return render(request, 'tours/index.html', context)


class DepartureView(View):
    def get(self, request, departure):
        tours_city = tours_city_dates(departure, tours)

        context = {'departures': departures, 'tours': tours, 'title': title,
                   'tours_count': tours_city['tours_count'], 'price': tours_city['price'],
                   'night': tours_city['night'], 'departure': departures[departure]}

        return render(request, 'tours/departure.html', context)


class TourView(View):
    def get(self, request, id):
        if id not in tours:
            raise Http404

        context = {'tour': tours[id], 'departures': departures, 'title': title}
        return render(request, 'tours/tour.html', context)


def my_handler404(request, exception=None):
    return render(request, '404.html')


def my_handler500(request, exception=None):
    return render(request, '500.html')
