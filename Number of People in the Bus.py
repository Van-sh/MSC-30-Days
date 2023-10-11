def number(bus_stops):
    result = 0
    for stop in bus_stops:
        result += stop[0] - stop[1]
    return result