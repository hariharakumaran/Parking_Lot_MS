from typing import Dict
from parking_spot import ParkingSpot
from vehicle import Vehicle
from vehicle_size import VehicleSize
from threading import Lock
from collections import defaultdict

class ParkingFloor:

    _lock = Lock()

    def __init__(self, floor_number: int):
        self.floor_number = floor_number
        self.spots: Dict[str, ParkingSpot] = {}

    def add_spot(self, spot: ParkingSpot):
        self.spots[spot.get_spot_id()] = spot

    def show_availabilty(self):
        with self._lock:
            available_spot = defaultdict(int)
            for spot in self.spots.values():
                if not spot.is_spot_occupied():
                    available_spot[spot.get_spot_size()] += 1
            
            for size in VehicleSize:
                print(f"Floor No: {self.floor_number}, Spot Size: {size}, Available spots: {available_spot[size]}")
    
    def find_available_spot(self, vehicle: Vehicle):
        with self._lock:
            available_spots = [spot for spot in self.spots.values()
                                if not spot.is_spot_occupied() and spot.can_fit_vehicle(vehicle)]
            if available_spots:
                available_spots = sorted(available_spots, key = lambda x:x.get_spot_size().value)
                return available_spots[0]
            return None