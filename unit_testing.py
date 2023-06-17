import unittest
from datetime import datetime

from carparts.engine import CapuletEngine, WilloughbyEngine, SternmanEngine
from carparts.battery import NubbinBattery, SpindlerBattery


class TestNubbinBattery(unittest.TestCase):
    def should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 5)

        battery = NubbinBattery(
            last_service_date=last_service_date, current_date=current_date
        )
        self.assertTrue(battery.needs_service())

    def should_not_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 1)

        battery = NubbinBattery(
            last_service_date=last_service_date, current_date=current_date
        )
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):
    def test_should_be_serviced(self):
        current_date = datetime.today().date()
        last_service_date = current_date.replace(year=current_date.year - 3)

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
