from abc import ABC, abstractmethod
from parking_floor import ParkingFloor
from vehicle import Vehicle
from typing import List

class ParkingStrategy(ABC):
    
    def __init__(self, floors: List[ParkingFloor]):
        self.floors = floors
    
    @abstractmethod
    def find_spot(self, vehicle: Vehicle):
        pass

class ClosestStrategy(ParkingStrategy):
    
    def find_spot(self, vehicle: Vehicle):
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle) 
            if spot:
                return spot
        return None

class FarthestStrategy(ParkingStrategy):

    def find_spot(self, vehicle: Vehicle):
        for floor in reversed(self.floors):
            spot = floor.find_available_spot(vehicle)
            if spot:
                return spot
        return None

class BestFitStrategy(ParkingStrategy):

    def find_spot(self, vehicle: Vehicle):
        best_fit = None
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle)

            if spot and (best_fit is None or spot.get_spot_size().value < best_fit.get_spot_size().value):
                best_fit = spot
        return best_fit