from parking_spot import ParkingSpot
from vehicle import Vehicle
from uuid import uuid4
from time import time

class ParkingTicket:

    def __init__(self, spot: ParkingSpot, vehicle: Vehicle):
        self.ticket_id = str(uuid4())
        self.spot = spot
        self.vehicle = vehicle
        self.entry_time = time()
        self.exit_time = None
    
    def get_ticket_id(self):
        return self.ticket_id
    
    def get_vehicle(self):
        return self.vehicle
    
    def get_spot(self):
        return self.spot
    
    def get_entry_time(self):
        return self.entry_time
    
    def get_exit_time(self):
        return self.exit_time
    
    def set_exit_time(self):
        self.exit_time = time()