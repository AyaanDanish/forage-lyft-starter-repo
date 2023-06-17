from car import Car
from carparts.engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from carparts.battery import NubbinBattery, SpindlerBattery
from carparts.tire import CarriganTire, OctoprimeTire


def CarFactory():
    @staticmethod
    def create_calliope(
        self,
        current_date,
        last_service_date,
        current_mileage,
        last_service_mileage,
        tire_sensor_readings,
    ):
        engine = CapuletEngine(self.current_mileage, self.last_service_mileage)
        battery = SpindlerBattery(self.last_service_date, self.current_date)
        tire = CarriganTire(self.tire_sensor_readings)

        return Car(engine, battery, tire)

    @staticmethod
    def create_glissade(
        self,
        current_date,
        last_service_date,
        current_mileage,
        last_service_mileage,
        tire_sensor_readings,
    ):
        engine = WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        battery = SpindlerBattery(self.last_service_date, self.current_date)
        tire = CarriganTire(self.tire_sensor_readings)

        return Car(engine, battery, tire)

    @staticmethod
    def create_palindrome(
        self, current_date, last_service_date, warning_light_on, tire_sensor_readings
    ):
        engine = SternmanEngine(self.last_service_date, self.warning_light_on)
        battery = SpindlerBattery(self.last_service_date, self.current_date)
        tire = OctoprimeTire(self.tire_sensor_readings)

        return Car(engine, battery, tire)

    @staticmethod
    def create_rorschach(
        self,
        current_date,
        last_service_date,
        current_mileage,
        last_service_mileage,
        tire_sensor_readings,
    ):
        engine = WilloughbyEngine(self.current_mileage, self.last_service_mileage)
        battery = NubbinBattery(self.last_service_date, self.current_date)
        tire = OctoprimeTire(self.tire_sensor_readings)

        return Car(engine, battery, tire)

    @staticmethod
    def create_thovex(
        self,
        current_date,
        last_service_date,
        current_mileage,
        last_service_mileage,
        tire_sensor_readings,
    ):
        engine = CapuletEngine(self.current_mileage, self.last_service_mileage)
        battery = NubbinBattery(self.last_service_date, self.current_date)
        tire = OctoprimeTire(self.tire_sensor_readings)

        return Car(engine, battery, tire)
