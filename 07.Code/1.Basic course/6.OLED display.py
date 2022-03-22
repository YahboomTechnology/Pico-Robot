from machine import Pin, I2C
from pico_car import SSD1306_I2C
import time
# set IIC pin
i2c=I2C(1, scl=Pin(15),sda=Pin(14), freq=100000)
# initialization oled
oled = SSD1306_I2C(128, 32, i2c)
# oled show hello at 0,0
oled.text('Hello', 0, 0)
oled.show()
oled.fill(0)
time.sleep(1)
# oled show World at 0,10
oled.text('World', 0, 10)
oled.show()
oled.fill(0)
time.sleep(1)
# oled show spot at 100,30
oled.pixel(100, 30, 1)
oled.show()
oled.fill(0)
time.sleep(1)
