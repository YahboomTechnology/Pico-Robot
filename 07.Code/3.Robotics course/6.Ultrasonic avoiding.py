import time
from machine import Pin, I2C, PWM
from pico_car import SSD1306_I2C, ultrasonic, pico_car, ws2812b

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
# Initialize music
CM = [0, 330, 350, 393, 441, 495, 556, 624]
#initialization ultrasonic
ultrasonic = ultrasonic()
#initialization oled
i2c=I2C(1, scl=Pin(15),sda=Pin(14), freq=100000)
oled = SSD1306_I2C(128, 32, i2c)

while True:
    #get distance
    distance = ultrasonic.Distance_accurate()
    print("distance is %d cm"%(distance) )
    #display distance
    oled.text('distance:', 0, 0)
    oled.text(str(distance), 75, 0)
    oled.show()
    oled.fill(0)
    #Control action
    if distance < 10:
        for i in range(num_leds):
            pixels.set_pixel(i,255,0,0)
        pixels.show()
        Motor.Car_Back(150,150)
        BZ.duty_u16(500)
        BZ.freq(CM[7])
        time.sleep(0.2)
        Motor.Car_Right(150,150)
        BZ.duty_u16(500)
        BZ.freq(CM[5])
        time.sleep(0.2)
        BZ.duty_u16(0)
    elif distance >= 10 and distance < 30:
        for i in range(num_leds):
            pixels.set_pixel(i,255,255,0)
        pixels.show()
        Motor.Car_Run(100,100)
    else:
        for i in range(num_leds):
            pixels.set_pixel(i,0,255,0)
        pixels.show()
        Motor.Car_Run(100,100)
    time.sleep(0.1)
