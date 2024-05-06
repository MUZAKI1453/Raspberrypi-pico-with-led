import machine
import utime

led = machine.Pin(7, machine.Pin.OUT)

while True:
    led.value(1)
    utime.sleep(2)
    led.value(0)
    utime.sleep(2)