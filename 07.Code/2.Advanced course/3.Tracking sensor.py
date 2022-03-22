from machine import Pin, I2C
from pico_car import SSD1306_I2C
import time
#initialization oled
i2c=I2C(1, scl=Pin(15),sda=Pin(14), freq=100000)
oled = SSD1306_I2C(128, 32, i2c)
#Define the tracking sensor, 1-4 from left to right
#recognize that black is 0 and white is 1
#Tracing_1 Tracing_2 Tracing_3 Tracing_4
#    2         3        4          5     
Tracing_1 = machine.Pin(2, machine.Pin.IN)
Tracing_2 = machine.Pin(3, machine.Pin.IN)
Tracing_3 = machine.Pin(4, machine.Pin.IN)
Tracing_4 = machine.Pin(5, machine.Pin.IN)

while True:
    oled.text('T1', 5, 0)
    oled.text('T2', 35, 0)
    oled.text('T3', 65, 0)
    oled.text('T4', 95, 0)
    print("T1: %d T2: %d T3: %d T4: %d "%(Tracing_1.value(),Tracing_2.value(),Tracing_3.value(),Tracing_4.value()))
    # Tracing1 display
    if Tracing_1.value() == 1:
        oled.text('1', 9, 10)
        for i in range(10):
            for j in range(10):
                oled.pixel(i+8, 20+j, 1)
    elif Tracing_1.value() == 0:
        oled.text('0', 9, 10)
        for i in range(10):
            oled.pixel(i+8, 20, 1)
            oled.pixel(i+8, 29, 1)
        for j in range(8):
            oled.pixel(8, 21+j, 1)
        for j in range(8):
            oled.pixel(17, 21+j, 1)
    # Tracing2 display        
    if Tracing_2.value() == 1:
        oled.text('1', 39, 10)
        for i in range(10):
            for j in range(10):
                oled.pixel(i+38, 20+j, 1)
    elif Tracing_2.value() == 0:
        oled.text('0', 39, 10)
        for i in range(10):
            oled.pixel(i+38, 20, 1)
            oled.pixel(i+38, 29, 1)
        for j in range(8):
            oled.pixel(38, 21+j, 1)
        for j in range(8):
            oled.pixel(47, 21+j, 1)
    # Tracing3 display        
    if Tracing_3.value() == 1:
        oled.text('1', 69, 10)
        for i in range(10):
            for j in range(10):
                oled.pixel(i+68, 20+j, 1)
    elif Tracing_3.value() == 0:
        oled.text('0', 69, 10)
        for i in range(10):
            oled.pixel(i+68, 20, 1)
            oled.pixel(i+68, 29, 1)
        for j in range(8):
            oled.pixel(68, 21+j, 1)
        for j in range(8):
            oled.pixel(77, 21+j, 1)
    # Tracing4 display        
    if Tracing_4.value() == 1:
        oled.text('1', 99, 10)
        for i in range(10):
            for j in range(10):
                oled.pixel(i+98, 20+j, 1)
    elif Tracing_4.value() == 0:
        oled.text('0', 99, 10)
        for i in range(10):
            oled.pixel(i+98, 20, 1)
            oled.pixel(i+98, 29, 1)
        for j in range(8):
            oled.pixel(98, 21+j, 1)
        for j in range(8):
            oled.pixel(107, 21+j, 1)
    oled.show()
    oled.fill(0)
    time.sleep(0.1)
