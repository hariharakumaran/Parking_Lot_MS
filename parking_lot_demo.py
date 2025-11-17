from parking_lot import ParkingLot
from parking_floor import ParkingFloor
from parking_spot import ParkingSpot
from vehicle_size import VehicleSize
from fee_strategy import VehicleBasedRateStrategy
from bike import Bike
from car import Car
from truck import Truck

class ParkingLotDemo:

    @staticmethod
    def run():
        #1
        parking_lot = ParkingLot.get_instance()

        floor1 = ParkingFloor(1)
        floor1.add_spot(ParkingSpot("F01S01", VehicleSize.SMALL))
        floor1.add_spot(ParkingSpot("F01M01", VehicleSize.MEDIUM))
        floor1.add_spot(ParkingSpot("F01L01", VehicleSize.LARGE))

        floor2 = ParkingFloor(2)
        floor2.add_spot(ParkingSpot("F02S01", VehicleSize.SMALL))
        floor2.add_spot(ParkingSpot("F02M01", VehicleSize.MEDIUM))

        parking_lot.add_floor(floor1)
        parking_lot.add_floor(floor2)

        parking_lot.set_fee_strategy(VehicleBasedRateStrategy())

        #2
        floor1.show_availabilty()
        floor2.show_availabilty()
        parking_lot.show_parked_vehicles()

        car = Car("TN81B5463")
        bike = Bike("TN01AC0751")
        truck = Truck("TN01X0001")

        car_ticket = parking_lot.park_vehicle(car)
        bike_ticket = parking_lot.park_vehicle(bike)
        truck_ticket = parking_lot.park_vehicle(truck)

        floor1.show_availabilty()

        truck2 = Truck("TN02D4567")
        failed_truck_ticket = parking_lot.park_vehicle(truck2)

        if car_ticket is not None:
            fee = parking_lot.unpark_vehicle(car)
            if fee is not None:
                print(f"Car {car.get_license()} parking fee: {fee:.2f}")

        print("\n--- Availability after one car leaves ---")
        floor1.show_availabilty()
        floor2.show_availabilty()
        parking_lot.show_parked_vehicles()

        bike2 = Bike("TN45E2234")
        bike2_ticket = parking_lot.park_vehicle(bike2)

        print("\n--- Availability after new bike comes ---")
        floor1.show_availabilty()
        floor2.show_availabilty()
        parking_lot.show_parked_vehicles()

if __name__ == "__main__":
    ParkingLotDemo.run()