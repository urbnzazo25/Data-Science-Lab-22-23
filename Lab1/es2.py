import json
import sys
from math import cos, acos, sin

def distance_coords(lat1, lng1, lat2, lng2):
    deg2rad = lambda x: x * 3.141592 / 180
    lat1, lng1, lat2, lng2 = map(deg2rad, [ lat1, lng1, lat2, lng2 ])
    R = 6378100 # Radius of the Earth, in meters
    return R * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lng1 - lng2))

if __name__ == '__main__':
    with open("toBike") as f:
     obj = json.load(f)
    d = dict(obj)

    numOnline = 0
    for station in d['network']['stations']:
        if station['extra']['status'] == 'online':
            numOnline += 1
    print(f"number of online stations: {numOnline}")

    numFreeBikes = 0
    for station in d['network']['stations']:
        numFreeBikes += station['free_bikes']
    print(f"Number of free bikes: {numFreeBikes}")

    numEmptySlots = 0
    for station in d['network']['stations']:
        numEmptySlots += station['empty_slots']
    print(f"Number of empty slots: {numEmptySlots}")

    coord = (45.0440925, 7.63941699999)
    closest = {'name': '', 'dist': sys.maxsize}
    for station in d['network']['stations']:
        dist = distance_coords(coord[0], coord[1], station['latitude'], station['longitude'])
        if dist < closest['dist']:
            closest['name'] = station['name']
            closest['dist'] = dist
    print(f"Closest distance to given coordinates: {closest}")