def tours_city_dates(departure, tours):
    tours_from_city = []
    price = []
    night = []
    for tour in tours.values():
        if departure in tour.values():
            tours_from_city.append(tour)
            price.append(tour['price'])
            night.append(tour['nights'])
    tours_count = len(tours_from_city)
    price = sorted(price)
    night = sorted(night)
    tours_city = {'tours_count': tours_count, 'price': price, 'night': night}
    return tours_city
