from pico_car import SSD1306_I2C, pico_car, ws2812b
from machine import Pin, I2C, ADC, PWM
import time

Motor = pico_car()
Motor.Car_Stop()
num_leds = 8  # Number of NeoPixels
# Pin where NeoPixels are connected
pixels = ws2812b(num_leds, 0)
pixels.fill(0,0,0)
pixels.show()
# set buzzer pin
BZ = PWM(Pin(22))
BZ.freq(1000)
CM = [0, 330, 350, 393, 441, 495, 556, 624]
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
    #Control action
    if sounds > 20000:
        while sounds > 10000:
            Motor.Car_Stop()
            sounds = Sound.read_u16()
            print(sounds)
            time.sleep(0.001)
        Motor.Car_Run(255,255)
        BZ.duty_u16(500)
        BZ.freq(CM[1])
        pixels.set_pixel(2,150,0,150)
        pixels.set_pixel(3,150,0,150)
        pixels.show()
        time.sleep(0.03)
        BZ.duty_u16(500)
        BZ.freq(CM[2])
        pixels.set_pixel(2,0,0,0)
        pixels.set_pixel(3,0,0,0)
        pixels.set_pixel(1,150,0,150)
        pixels.set_pixel(4,150,0,150)
        pixels.show()
        time.sleep(0.03)
        BZ.duty_u16(500)
        BZ.freq(CM[3])
        pixels.set_pixel(1,0,0,0)
        pixels.set_pixel(4,0,0,0)
        pixels.set_pixel(0,150,0,150)
        pixels.set_pixel(5,150,0,150)
        pixels.show()
        time.sleep(0.03)
        BZ.duty_u16(500)
        BZ.freq(CM[4])
        pixels.set_pixel(0,0,0,0)
        pixels.set_pixel(5,0,0,0)
        pixels.set_pixel(6,150,0,150)
        pixels.set_pixel(7,150,0,150)
        pixels.show()
        time.sleep(0.03)
        BZ.duty_u16(500)
        BZ.freq(CM[5])
        pixels.set_pixel(0,0,0,0)
        pixels.set_pixel(5,0,0,0)
        pixels.set_pixel(6,150,0,150)
        pixels.set_pixel(7,150,0,150)
        pixels.show()
        time.sleep(0.03)
        BZ.duty_u16(500)
        BZ.freq(CM[6])
        pixels.set_pixel(6,0,0,0)
        pixels.set_pixel(7,0,0,0)
        pixels.show()
        BZ.duty_u16(0)
        sounds = 0
        oled.show()
        oled.fill(0)
    else:
        Motor.Car_Stop()
        oled.show()
        oled.fill(0)
    time.sleep(0.01)
