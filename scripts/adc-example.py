from machine import Timer
import machine
import time

time.sleep(1)

adc = machine.ADC(1)
start = time.ticks_ms()
samps = 10000
for i in range(samps):
    adc.read()
delta = time.ticks_diff(time.ticks_ms(), start)
print("Frequency:" + str(samps/(delta/1000)) + " Hz")
