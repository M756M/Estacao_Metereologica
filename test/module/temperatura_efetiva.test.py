import sys;
sys.path.append("src")

from temperatura_efetiva import effectiveTemperature, Measurement;

print(effectiveTemperature(Measurement.generate((1, 40), (1, 60), (1, 5))))