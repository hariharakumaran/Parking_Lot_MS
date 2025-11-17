from vehicle import Vehicle
from vehicle_size import VehicleSize

class Truck(Vehicle):
    def __init__(self, license_no):
        super().__init__(license_no, VehicleSize.LARGE)