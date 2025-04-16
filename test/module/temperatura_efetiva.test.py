import sys;
sys.path.append("/Users/20231PF.INF_I0007/estacao/src")

from temperatura_efetiva import effectiveTemperature, Measurement;

print(effectiveTemperature(Measurement.generate((1, 5), (1, 5), (1, 5))))