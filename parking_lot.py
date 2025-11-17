from threading import Lock
from parking_floor import ParkingFloor
from parking_strategy import ClosestStrategy, BestFitStrategy
from parking_ticket import ParkingTicket
from fee_strategy import FeeStrategy, StandardRateStrategy
from vehicle import Vehicle
from typing import List

class ParkingLot:

    _instance = None
    _main_lock = Lock()
    
    def __init__(self):
        if ParkingLot._instance is not None:
            raise Exception("This is Singleton Class")
        self.parking_floor: List[ParkingFloor] = []
        self.parking_strategy = BestFitStrategy(self.parking_floor)
        self.fee_strategy = StandardRateStrategy()
        self.active_tickets = {}

    @staticmethod
    def get_instance():
        if ParkingLot._instance is None:
            with ParkingLot._main_lock:
                if ParkingLot._instance is None:
                    ParkingLot._instance = ParkingLot()
        return ParkingLot._instance
    
    def add_floor(self, floor: ParkingFloor):
        self.parking_floor.append(floor)
    
    def set_fee_strategy(self, strategy: FeeStrategy):
        self.fee_strategy = strategy

    def park_vehicle(self, vehicle: Vehicle):
        with self._main_lock:
            spot = self.parking_strategy.find_spot(vehicle)
            if spot:
                spot.allocate_spot(vehicle)
                ticket = ParkingTicket(spot, vehicle)
                self.active_tickets[vehicle.get_license()] = ticket
                print(f"{vehicle.__class__.__name__} {vehicle.get_license()} parked at spot {spot.get_spot_id()}")
                return ticket
            else:
                print(f"No spot is available for {vehicle.__class__.__name__}: {vehicle.get_license()}")
                return None
    
    def unpark_vehicle(self, vehicle: Vehicle):
        with self._main_lock:
            parking_ticket: ParkingTicket = self.active_tickets.pop(vehicle.get_license(), None)
            if parking_ticket:
                parking_ticket.set_exit_time()
                parking_ticket.get_spot().deallocate_spot()
                fee = self.fee_strategy.calculate_fee(parking_ticket)
                print(f"{vehicle.__class__.__name__} {vehicle.get_license()} unparked from spot {parking_ticket.get_spot().get_spot_id()}")
                return fee
            else:
                print(f"Ticket not found for {vehicle.__class__.__name__} {vehicle.get_license()}")
                return None
    
    def show_parked_vehicles(self):
        if self.active_tickets:
            for ticket in self.active_tickets.values():
                vehicle = ticket.get_vehicle()
                print(f"{vehicle.__class__.__name__} {vehicle.get_license()} parked at {ticket.get_spot().get_spot_id()}")
        else:
            print("No Vehicles are parked at the moment")