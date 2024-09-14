import machine 
import time 
led_onboard = machine.Pin(25, machine.Pin.OUT)

while True: 
    led_onboard.value(1) 
    time.sleep(1) 
    led_onboard.value(0) 
    time.sleep(1)