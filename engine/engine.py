from abc import ABC, abstractmethod


class Engine(ABC):
    @abstractmethod
    def needs_service(self):
        pass

class CapuletEngine(Engine, ABC):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000

class WilloughbyEngine(Engine, ABC):
    def __init__(self, current_mileage, last_service_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000


class SternmanEngine(Engine, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        return self.warning_light_is_on
