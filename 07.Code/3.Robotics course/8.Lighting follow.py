import time
from machine import Pin, I2C, PWM, ADC
from pico_car import SSD1306_I2C, pico_car, ws2812b

Motor = pico_car()
Motor.Car_Stop()
num_leds = 8  # Number of NeoPixels
# Pin where NeoPixels are connected
pixels = ws2812b(num_leds, 0)
pixels.fill(0,0,0) 
pixels.show()
#Light1 -> GP27
#Light2 -> GP26
light1 = machine.ADC(27)
light2 = machine.ADC(26)
#initialization oled
i2c=I2C(1, scl=Pin(15),sda=Pin(14), freq=100000)
oled = SSD1306_I2C(128, 32, i2c)
light_down = 0.9
light_up = 1.1

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
    #Control action
    if LightS1 > (LightS2*light_down) and LightS1 < (LightS2*light_up):
        Motor.Car_Run(120,120)
        for i in range(num_leds):
            pixels.set_pixel(i,150,150,150)
        pixels.show()
    elif LightS2 > (LightS1*light_down) and LightS2 < (LightS1*light_up):
        Motor.Car_Run(120,120)
        for i in range(num_leds):
            pixels.set_pixel(i,150,150,150)
        pixels.show()
    elif LightS1 > (LightS2*light_up) or LightS2 < (LightS1*light_down):
        Motor.Car_Run(120,0)
        pixels.fill(0,0,0) 
        pixels.set_pixel(0,150,0,150)
        pixels.set_pixel(1,150,0,150)
        pixels.set_pixel(2,150,0,150)
        pixels.set_pixel(7,150,0,150)
        pixels.show()
    elif LightS2 > (LightS1*light_up) or LightS1 < (LightS2*light_down):
        Motor.Car_Run(0,120)
        pixels.fill(0,0,0) 
        pixels.set_pixel(3,150,0,150)
        pixels.set_pixel(4,150,0,150)
        pixels.set_pixel(5,150,0,150)
        pixels.set_pixel(6,150,0,150)
        pixels.show()
    else:
        Motor.Car_Stop()
    oled.show()
    oled.fill(0)
    time.sleep(0.01)
