from abc import ABC, abstractmethod
from parking_ticket import ParkingTicket

class FeeStrategy(ABC):

    @abstractmethod
    def calculate_fee(self, ticket: ParkingTicket):
        pass

class StandardRateStrategy(FeeStrategy):

    hourly_rate: int = 10

    def calculate_fee(self, ticket: ParkingTicket):
        parked_hours = ((ticket.exit_time - ticket.entry_time) // (60 * 60)) + 1
        return parked_hours * self.hourly_rate

class VehicleBasedRateStrategy(FeeStrategy):

    hourly_rate: int = 10

    def calculate_fee(self, ticket: ParkingTicket):
        vehicle_rate = ticket.get_vehicle().get_vehicle_size().value
        parked_hours = ((ticket.exit_time - ticket.entry_time) // (60 * 60)) + 1
        return vehicle_rate * parked_hours * self.hourly_rate 