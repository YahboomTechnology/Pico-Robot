from machine import Pin, I2C, ADC
from pico_car import SSD1306_I2C
import time

#initialization oled
i2c=I2C(1, scl=Pin(15),sda=Pin(14), freq=100000)
oled = SSD1306_I2C(128, 32, i2c)
#initialization ADC
Quantity_of_electricity = machine.ADC(28)

while True:
    #Display power on OLED
    #Under 20000, there is no power at all
    oled.text('Battery:', 0, 0)
    oled.text(str(Quantity_of_electricity.read_u16()), 65, 0)
    oled.show()
    oled.fill(0)
    time.sleep(0.1)
