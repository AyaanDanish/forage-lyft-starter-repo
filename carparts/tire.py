from abc import ABC, abstractmethod


class Tire(ABC):
    @abstractmethod
    def needs_service(self):
        pass


class CarriganTire(Tire):
    def __init__(self, tire_sensor_readings):
        self.tire_sensor_readings = tire_sensor_readings

    def needs_service(self):
        for reading in self.tire_sensor_readings:
            if reading >= 0.9:
                return True
        return False


class OctoprimeTire(Tire):
    def __init__(self, tire_sensor_readings):
        self.tire_sensor_readings = tire_sensor_readings

    def needs_service(self):
        sum = 0
        for reading in self.tire_sensor_readings:
            sum += reading
        return sum >= 3
