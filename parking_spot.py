from vehicle_size import VehicleSize
from vehicle import Vehicle
from threading import Lock

class ParkingSpot:

    def __init__(self, spot_id: str, spot_size: VehicleSize):
        self.spot_id = spot_id
        self.spot_size = spot_size
        self.is_occupied = False
        self.parked_vehicle = None
        self.lock = Lock()
    
    def get_spot_id(self):
        return self.spot_id
    
    def is_spot_occupied(self):
        return self.is_occupied
    
    def get_spot_size(self):
        return self.spot_size
    
    def allocate_spot(self, vehicle: Vehicle):
        with self.lock:
            self.is_occupied = True
            self.parked_vehicle = vehicle
    
    def deallocate_spot(self):
        with self.lock:
            self.is_occupied = False
            self.parked_vehicle = None
    
    def can_fit_vehicle(self, vehicle: Vehicle):
        if vehicle.get_vehicle_size() == VehicleSize.SMALL:
            return self.get_spot_size() == VehicleSize.SMALL or self.get_spot_size() == VehicleSize.MEDIUM or self.get_spot_size() == VehicleSize.LARGE
        elif vehicle.get_vehicle_size() == VehicleSize.MEDIUM:
            return self.get_spot_size() == VehicleSize.MEDIUM or self.get_spot_size() == VehicleSize.LARGE
        elif vehicle.get_vehicle_size() == VehicleSize.LARGE:
            return self.get_spot_size() == VehicleSize.LARGE
        else:
            return None