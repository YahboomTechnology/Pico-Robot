import time
from machine import Pin, I2C
from pico_car import SSD1306_I2C, ir
#initialization ir
Ir = ir()
#initialization oled
i2c=I2C(1, scl=Pin(15),sda=Pin(14), freq=100000)
oled = SSD1306_I2C(128, 32, i2c)

while True:
    #get value
    value = Ir.Getir()
    time.sleep(0.01)
    if value != None:
        print(value)
        #display press
        if value == 0:
            while value == 0:
                value = Ir.Getir()
            oled.text('Press:Power', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 1:
            while value == 1:
                value = Ir.Getir()
            oled.text('Press:Up', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 2:
            while value == 2:
                value = Ir.Getir()
            oled.text('Press:Light', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 4:
            while value == 4:
                value = Ir.Getir()
            oled.text('Press:Left', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 5:
            while value == 5:
                value = Ir.Getir()
            oled.text('Press:Sound', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 6:
            while value == 6:
                value = Ir.Getir()
            oled.text('Press:Right', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 8:
            while value == 8:
                value = Ir.Getir()
            oled.text('Press:Turn Left', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 9:
            while value == 9:
                value = Ir.Getir()
            oled.text('Press:Down', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 10:
            while value == 10:
                value = Ir.Getir()
            oled.text('Press:Turn Right', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 12:
            while value == 12:
                value = Ir.Getir()
            oled.text('Press:+', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 13:
            while value == 13:
                value = Ir.Getir()
            oled.text('Press:0', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 14:
            while value == 14:
                value = Ir.Getir()
            oled.text('Press:-', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 16:
            while value == 16:
                value = Ir.Getir()
            oled.text('Press:1', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 17:
            while value == 17:
                value = Ir.Getir()
            oled.text('Press:2', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 18:
            while value == 18:
                value = Ir.Getir()
            oled.text('Press:3', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 20:
            while value == 20:
                value = Ir.Getir()
            oled.text('Press:4', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 21:
            while value == 21:
                value = Ir.Getir()
            oled.text('Press:5', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 22:
            while value == 22:
                value = Ir.Getir()
            oled.text('Press:6', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 24:
            while value == 24:
                value = Ir.Getir()
            oled.text('Press:7', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 25:
            while value == 25:
                value = Ir.Getir()
            oled.text('Press:8', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 26:
            while value == 26:
                value = Ir.Getir()
            oled.text('Press:9', 0, 0)
            oled.show()
            oled.fill(0)
        value = None

