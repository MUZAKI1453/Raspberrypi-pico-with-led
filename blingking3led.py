import machine
import utime

ledRed = machine.Pin(7, machine.Pin.OUT)
ledYellow = machine.Pin(8, machine.Pin.OUT)
ledGreen = machine.Pin(9, machine.Pin.OUT) 

while True:
    ledRed.value(1)
    ledYellow.value(0)
    ledGreen.value(0)
    utime.sleep(2)
    
    ledRed.value(0)
    ledYellow.value(1)
    ledGreen.value(0)
    utime.sleep(2)

    ledRed.value(0)
    ledYellow.value(0)
    ledGreen.value(1)
    utime.sleep(2)

