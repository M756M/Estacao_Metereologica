from random import random;
from math import ceil, modf;

class Measurement:
    temperature: float
    relativeMoisture: float
    airSpeed: float
    
    def __init__(self, temperature = 0.0, relativeMoisture = 0.0, airSpeed = 0.0):
        self.temperature = temperature or 0
        self.relativeMoisture = relativeMoisture or 0
        self.airSpeed = airSpeed or 0

        return
    
    def __str__(self): return f"(T = {self.temperature} °C, h = {self.relativeMoisture}%, v = {self.airSpeed} m/s)"

    def __iter__(self): return [self.temperature, self.relativeMoisture, self.airSpeed].__iter__()

    def setMeasurement(self, temperature, relativeMoisture, airSpeed):
        self.temperature = temperature
        self.relativeMoisture = relativeMoisture
        self.airSpeed = airSpeed

        return self
    
    @staticmethod
    def generate(temperature: tuple[float, float], relativeMoisture: tuple[float, float], airSpeed: tuple[float, float]) -> list['Measurement']:
        dTemperature = temperature[1] - temperature[0]
        dRelativeMoisture = relativeMoisture[1] - relativeMoisture[0]
        dAirSpeed = airSpeed[1] - airSpeed[0]
        
        P = [Measurement() for _ in range(dTemperature * dRelativeMoisture * dAirSpeed)]

        for i in range(1, len(P)):
            _temperature = random() * dTemperature
            _relativeMoisture = random() * dRelativeMoisture
            _airSpeed = random() * dAirSpeed

            P[i] = Measurement(float(f"{_temperature: .2f}"), float(f"{_relativeMoisture: .2f}"), float(f"{_airSpeed: .2f}"))
        return P

def effectiveTemperature(*measurements: Measurement) -> list[float]:
    class PrintableList(list):
        def __str__(self):
            str = "[\n"

            for i in range(0, len(self), 3):
                if(len(self) - i < 3):
                    str += "\u0020"
                    for j in range(0, len(self) - i): str += f"{self[i + j]}{"" if j == len(self) - i - 1 else ", "}"
                else: str += f"\u0020{self[i]}, {self[i + 1]}, {self[i + 2]}{"" if i == len(self) - 3 else ",\n"}"
            return str + "\n]"

   
    V = lambda v: 1/(1.76 + 1.4 * pow(v, 0.75))
    H = lambda h: 1 - h/100

    flatMeasurements = []

    for m in measurements:
        if(type(m) == tuple or type(m) == list):
            for x in m: flatMeasurements.append(x)
        else: flatMeasurements.append(m)

    result = [
        37 - (37 - m.temperature)/(0.68 - 0.0014 * m.relativeMoisture + V(m.airSpeed)) - 0.29 * m.temperature * H(m.relativeMoisture) for m in flatMeasurements
    ]

    return PrintableList([float(f"{f: .2f}") for f in result])