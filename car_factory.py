from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

from tyre.carrigan_tyre import CarriganTyre
from tyre.octoprime_tyre import OctoprimeTyre

from car import Car


class CarFactory:

    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, tyre_wear):
        # create engine
        engine = CapuletEngine(current_mileage, last_service_mileage)

        # create battery
        battery = SpindlerBattery(last_service_date, current_date)

        # create tyre
        tyres = CarriganTyre(tyre_wear)

        # create car
        car = Car(engine, battery, tyres)

        return car

    @staticmethod
    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, tyre_wear):
        # create engine
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        # create battery
        battery = SpindlerBattery(last_service_date, current_date)

        # create tyres
        tyres = OctoprimeTyre(tyre_wear)

        # create car
        car = Car(engine, battery, tyres)

        return car

    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, tyre_wear):
        # create engine
        engine = SternmanEngine(warning_light_on)

        # create battery
        battery = SpindlerBattery(last_service_date, current_date)

        # create tyres
        tyres= OctoprimeTyre(tyre_wear)

        # create car
        car = Car(engine, battery, tyres)

        return car
    
    @staticmethod
    def create_roschach(current_date, last_service_date, current_mileage, last_service_mileage, tyre_wear):
        # create engine
        engine = WilloughbyEngine(current_mileage, last_service_mileage)

        # create battery
        battery =  NubbinBattery(last_service_date, current_date)

        # create tyres
        tyres = CarriganTyre(tyre_wear)

        # create car
        car = Car(engine, battery, tyres)

        return car
        
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, tyre_wear):
        # create engine
        engine = CapuletEngine(current_mileage, last_service_mileage)

        # create battery
        battery =  NubbinBattery(last_service_date, current_date)

        # create tyres
        tyres = OctoprimeTyre(tyre_wear)

        # create car
        car = Car(engine, battery, tyres)

        return car

    