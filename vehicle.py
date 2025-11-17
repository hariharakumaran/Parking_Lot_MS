from abc import ABC
from vehicle_size import VehicleSize

class Vehicle(ABC):
    def __init__(self, license_no: str, vehicle_size: VehicleSize):
        self.license_no = license_no
        self.vehicle_size = vehicle_size
    
    def get_license(self):
        return self.license_no
    
    def get_vehicle_size(self):
        return self.vehicle_size