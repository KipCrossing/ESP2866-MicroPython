from time import sleep_ms
from machine import Pin
print("Run: main.py")

# GPIO16 (D0) is the internal LED for NodeMCU
led = Pin(16, Pin.OUT)


def led_toggle():
    led.value(not led.value())


while True:
    led_toggle()
    sleep_ms(200)
