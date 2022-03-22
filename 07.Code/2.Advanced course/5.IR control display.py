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
        if value == 69:
            while value == 69:
                value = Ir.Getir()
            oled.text('Press:Power', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 71:
            while value == 71:
                value = Ir.Getir()
            oled.text('Press:MENU', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 68:
            while value == 68:
                value = Ir.Getir()
            oled.text('Press:TEST', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 64:
            while value == 64:
                value = Ir.Getir()
            oled.text('Press:+', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 67:
            while value == 67:
                value = Ir.Getir()
            oled.text('Press:BACK', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 7:
            while value == 7:
                value = Ir.Getir()
            oled.text('Press:<<', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 9:
            while value == 9:
                value = Ir.Getir()
            oled.text('Press:>>', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 21:
            while value == 21:
                value = Ir.Getir()
            oled.text('Press:>', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 25:
            while value == 25:
                value = Ir.Getir()
            oled.text('Press:-', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 13:
            while value == 13:
                value = Ir.Getir()
            oled.text('Press:C', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 22:
            while value == 22:
                value = Ir.Getir()
            oled.text('Press:0', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 12:
            while value == 12:
                value = Ir.Getir()
            oled.text('Press:1', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 24:
            while value == 24:
                value = Ir.Getir()
            oled.text('Press:2', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 94:
            while value == 94:
                value = Ir.Getir()
            oled.text('Press:3', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 8:
            while value == 8:
                value = Ir.Getir()
            oled.text('Press:4', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 28:
            while value == 28:
                value = Ir.Getir()
            oled.text('Press:5', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 90:
            while value == 90:
                value = Ir.Getir()
            oled.text('Press:6', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 66:
            while value == 66:
                value = Ir.Getir()
            oled.text('Press:7', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 82:
            while value == 82:
                value = Ir.Getir()
            oled.text('Press:8', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 74:
            while value == 74:
                value = Ir.Getir()
            oled.text('Press:9', 0, 0)
            oled.show()
            oled.fill(0)
        value = None

