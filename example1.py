#!/usr/bin/env python
from ina219 import INA219
from ina219 import DeviceRangeError
from time import sleep, gmtime, strftime

SHUNT_OHMS = 0.1

def read():
    ina = INA219(SHUNT_OHMS, busnum=3)
    ina.configure()
    while True:
        voltage = ina.voltage()
        now = strftime("%Y-%m-%d %H:%M:%S", gmtime())
        try:
            current = ina.current()
            power = ina.power()
            shunt_voltage = ina.shunt_voltage()
            print "[%s] -- Bus Voltage(V): %.3f \t Bus Current(mA): %.3f \t Power(mW): %.3f \t Shunt Voltage(mV): %.3f" % (now, voltage, current, power, shunt_voltage)
        except DeviceRangeError as e:
        # Current out of device range with specified shunt resister
            print e
        sleep(1)


if __name__ == "__main__":
    read()
