from pico_car import ds, SSD1306_I2C
from machine import Pin, I2C, ADC
import time

#initialization oled
i2c=I2C(1, scl=Pin(15),sda=Pin(14), freq=100000)
oled = SSD1306_I2C(128, 32, i2c)
#Light1 -> GP27
#Light2 -> GP26
light1 = machine.ADC(27)
light2 = machine.ADC(26)

while True:
    #get value
    LightS1 = light1.read_u16()
    LightS2 = light2.read_u16()
    print("light1 is %d"%(LightS1) )
    print("light2 is %d"%(LightS2) )
    #Display sound on OLED
    oled.text('Light1:', 0, 0)
    oled.text(str(LightS1), 60, 0)
    oled.text('Light2:', 0, 10)
    oled.text(str(LightS2), 60, 10)
    oled.show()
    oled.fill(0)
    time.sleep(0.5)
