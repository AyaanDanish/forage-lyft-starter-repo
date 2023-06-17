from datetime import datetime

from engine.capulet_engine import CapuletEngine


class Calliope(CapuletEngine):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery