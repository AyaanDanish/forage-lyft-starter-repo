from car import Car
from engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from battery import NubbinBattery, SpindlerBattery


def CarFactory():
    def create_calliope(
        self, current_date, last_service_date, current_mileage, last_service_mileage
    ):
        engine = CapuletEngine(self.current_mileage, self.last_service_mileage)
        battery = SpindlerBattery(self.last_service_date, self.current_date)
        return Car(engine, battery)

    def create_glissade(
        self, current_date, last_service_date, current_mileage, last_service_mileage
    ):
        engine = WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        battery = SpindlerBattery(self.last_service_date, self.current_date)
        return Car(engine, battery)

    def create_palindrome(self, current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(self.last_service_date, self.warning_light_on)
        battery = SpindlerBattery(self.last_service_date, self.current_date)
        return Car(engine, battery)

    def create_rorschach(
        self, current_date, last_service_date, current_mileage, last_service_mileage
    ):
        engine = WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        battery = NubbinBattery(self.last_service_date, self.current_date)
        return Car(engine, battery)

    def create_thovex(
        self, current_date, last_service_date, current_mileage, last_service_mileage
    ):
        engine = CapuletEngine(self.current_mileage, self.last_service_mileage)
        battery = NubbinBattery(self.last_service_date, self.current_date)
        return Car(engine, battery)
