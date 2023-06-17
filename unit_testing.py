import unittest
from datetime import datetime

from carparts.engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from carparts.battery import NubbinBattery, SpindlerBattery
from carparts.tire import CarriganTire, OctoprimeTire


class TestNubbinBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)

        battery = NubbinBattery(
            last_service_date=last_service_date, current_date=current_date
        )
        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        battery = NubbinBattery(
            last_service_date=last_service_date, current_date=current_date
        )
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 4)

        battery = SpindlerBattery(
            last_service_date=last_service_date, current_date=current_date
        )
        self.assertTrue(battery.needs_service())

    def test_should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        battery = SpindlerBattery(
            last_service_date=last_service_date, current_date=current_date
        )
        self.assertFalse(battery.needs_service())


class TestCapuletEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        engine = CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        current_mileage = 10000
        last_service_mileage = 0

        engine = CapuletEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        engine = WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        current_mileage = 10000
        last_service_mileage = 0

        engine = WilloughbyEngine(
            current_mileage=current_mileage, last_service_mileage=last_service_mileage
        )
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):
    def test_should_be_serviced(self):
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on=warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_should_not_be_serviced(self):
        warning_light_is_on = True

        engine = SternmanEngine(warning_light_is_on=warning_light_is_on)
        self.assertFalse(engine.needs_service())


class TestCarriganTire(unittest.TestCase):
    def test_should_be_serviced(self):
        tire_sensor_readings = [0.1, 0.5, 0.3, 0.9]

        tire = CarriganTire(tire_sensor_readings=tire_sensor_readings)
        self.assertTrue(tire.needs_service())

    def test_should_not_be_serviced(self):
        tire_sensor_readings = [0.1, 0.5, 0.3, 0.2]

        tire = CarriganTire(tire_sensor_readings=tire_sensor_readings)
        self.assertFalse(tire.needs_service())


class TestOctoprimeTire(unittest.TestCase):
    def test_should_be_serviced(self):
        tire_sensor_readings = [1, 1, 1, 0.1]

        tire = OctoprimeTire(tire_sensor_readings=tire_sensor_readings)
        self.assertTrue(tire.needs_service())

    def test_should_not_be_serviced(self):
        tire_sensor_readings = [0.1, 0.5, 0.3, 0.2]

        tire = OctoprimeTire(tire_sensor_readings=tire_sensor_readings)
        self.assertFalse(tire.needs_service())
