from pico_car import SSD1306_I2C
from machine import Pin, I2C, ADC
import time
#initialization oled
i2c=I2C(1, scl=Pin(15),sda=Pin(14), freq=100000)
oled = SSD1306_I2C(128, 32, i2c)
#initialization ADC
Sound = machine.ADC(27)

while True:
    #get value
    sounds = Sound.read_u16()
    print(sounds)
    oled.text('Sound:', 0, 0)
    oled.text(str(sounds), 50, 0)
    #Display sound on OLED
    for i in range(10):
        oled.pixel(i, 30, 1)
        oled.pixel(i, 29, 1)
    if sounds > 5000:
        for i in range(10):
            for j in range(4):
                oled.pixel(i+10, 27+j, 1)
    if sounds > 10000:
        for i in range(10):
            for j in range(10):
                oled.pixel(i+20, 21+j, 1)
    if sounds > 20000:
        for i in range(10):
            for j in range(20):
                oled.pixel(i+30, 11+j, 1)
    oled.show()
    oled.fill(0)
    time.sleep(0.1)
