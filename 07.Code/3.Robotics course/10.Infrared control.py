import time
from machine import Pin, I2C, PWM, Timer
from pico_car import SSD1306_I2C, ir, pico_car, ws2812b

Motor = pico_car()
Motor.Car_Stop()
num_leds = 8  # Number of NeoPixels
# Pin where NeoPixels are connected
pixels = ws2812b(num_leds, 0)
# Set all led off
pixels.fill(0,0,0)
pixels.show()
# set buzzer pin
BZ = PWM(Pin(22))
BZ.freq(1000)
#initialization ir
Ir = ir()
#initialization oled
i2c=I2C(1, scl=Pin(15),sda=Pin(14), freq=100000)
oled = SSD1306_I2C(128, 32, i2c)
#define Timer
tim = Timer()
times_ = 0
def tick(timer):
    global times_
    times_ = times_ + 1
    if times_ > 100:
        times_ = 0
#set timer frequency 20
tim.init(freq = 20,mode = Timer.PERIODIC,callback = tick)

while True:
    #get value
    value = Ir.Getir()
    time.sleep(0.01)
    if value != None:
        print(value)
        #display press
        if value == 1:
            i = 0
            while value == 1:
                value = Ir.Getir()
                Motor.Car_Run(255,255)
                if times_ > 1:
                    times_ = 0
                    if i == 0:
                        pixels.set_pixel(2,150,0,150)
                        pixels.set_pixel(3,150,0,150)
                        i = 1
                    elif i == 1:
                        pixels.set_pixel(2,0,0,0)
                        pixels.set_pixel(3,0,0,0)
                        pixels.set_pixel(1,150,0,150)
                        pixels.set_pixel(4,150,0,150)
                        i = 2
                    elif i == 2:
                        pixels.set_pixel(1,0,0,0)
                        pixels.set_pixel(4,0,0,0)
                        pixels.set_pixel(0,150,0,150)
                        pixels.set_pixel(5,150,0,150)
                        i = 3
                    elif i == 3:
                        pixels.set_pixel(0,0,0,0)
                        pixels.set_pixel(5,0,0,0)
                        pixels.set_pixel(6,150,0,150)
                        pixels.set_pixel(7,150,0,150)
                        i = 4
                    elif i == 4:
                        pixels.set_pixel(0,0,0,0)
                        pixels.set_pixel(5,0,0,0)
                        pixels.set_pixel(6,150,0,150)
                        pixels.set_pixel(7,150,0,150)
                        i = 5
                    elif i == 5:
                        pixels.set_pixel(6,0,0,0)
                        pixels.set_pixel(7,0,0,0)
                        i = 0
                    pixels.show()
            Motor.Car_Stop()
            oled.text('Run', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 4:
            i = 0
            while value == 4:
                value = Ir.Getir()
                Motor.Car_Left(130,130)
                if times_ > 1:
                    times_ = 0
                    if i == 0:
                        pixels.set_pixel(7,0,0,0)
                        pixels.set_pixel(0,150,0,150)
                        i = i + 1
                    else:
                        pixels.set_pixel(i-1,0,0,0)
                        pixels.set_pixel(i,150,0,150)
                        i = i + 1
                        if i == 8:
                            i = 0
                    pixels.show()
            Motor.Car_Stop()
            oled.text('Left', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 6:
            i = 8
            while value == 6:
                value = Ir.Getir()
                Motor.Car_Right(130,130)
                if times_ > 1:
                    times_ = 0
                    if i == 8:
                        pixels.set_pixel(7,150,0,150)
                        pixels.set_pixel(0,0,0,0)
                        i = i - 1
                    else:
                        pixels.set_pixel(i-1,150,0,150)
                        pixels.set_pixel(i,0,0,0)
                        i = i - 1
                        if i == 0:
                            i = 8
                    pixels.show()
            Motor.Car_Stop()
            oled.text('Right', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 5:
            while value == 5:
                value = Ir.Getir()
                BZ.duty_u16(500)
                BZ.freq(624)
            BZ.duty_u16(0)
            oled.text('Buzzer', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 9:
            i = 0
            while value == 9:
                value = Ir.Getir()
                Motor.Car_Back(255,255)
                if times_ > 1:
                    times_ = 0
                    if i == 0:
                        pixels.set_pixel(6,150,0,150)
                        pixels.set_pixel(7,150,0,150)
                        i = 1
                    elif i == 1:
                        pixels.set_pixel(6,0,0,0)
                        pixels.set_pixel(7,0,0,0)
                        pixels.set_pixel(0,150,0,150)
                        pixels.set_pixel(5,150,0,150)
                        i = 2
                    elif i == 2:
                        pixels.set_pixel(0,0,0,0)
                        pixels.set_pixel(5,0,0,0)
                        pixels.set_pixel(1,150,0,150)
                        pixels.set_pixel(4,150,0,150)
                        i = 3
                    elif i == 3:
                        pixels.set_pixel(1,0,0,0)
                        pixels.set_pixel(4,0,0,0)
                        pixels.set_pixel(2,150,0,150)
                        pixels.set_pixel(3,150,0,150)
                        i = 4
                    elif i == 4:
                        pixels.set_pixel(1,0,0,0)
                        pixels.set_pixel(4,0,0,0)
                        pixels.set_pixel(2,150,0,150)
                        pixels.set_pixel(3,150,0,150)
                        i = 5
                    elif i == 5:
                        pixels.set_pixel(2,0,0,0)
                        pixels.set_pixel(3,0,0,0)
                        i = 0
                    pixels.show()
            Motor.Car_Stop()
            oled.text('Back', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 16:
            while value == 16:
                value = Ir.Getir()
            for i in range(num_leds):
                pixels.set_pixel(i,255,0,0)
            pixels.show()
            oled.text('Red', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 17:
            while value == 17:
                value = Ir.Getir()
            for i in range(num_leds):
                pixels.set_pixel(i,0,255,0)
            pixels.show()
            oled.text('Green', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 18:
            while value == 18:
                value = Ir.Getir()
            for i in range(num_leds):
                pixels.set_pixel(i,0,0,255)
            pixels.show()
            oled.text('Blue', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 20:
            while value == 20:
                value = Ir.Getir()
            for i in range(num_leds):
                pixels.set_pixel(i,255,255,0)
            pixels.show()
            oled.text('Yellow', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 21:
            while value == 21:
                value = Ir.Getir()
            for i in range(num_leds):
                pixels.set_pixel(i,0,255,255)
            pixels.show()
            oled.text('Cyan', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 22:
            while value == 22:
                value = Ir.Getir()
            for i in range(num_leds):
                pixels.set_pixel(i,255,0,255)
            pixels.show()
            oled.text('Purple', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 24:
            while value == 24:
                value = Ir.Getir()
            for i in range(num_leds):
                pixels.set_pixel(i,255,255,255)
            pixels.show()
            oled.text('White', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 25:
            while value == 25:
                value = Ir.Getir()
            for i in range(num_leds):
                pixels.set_pixel(i,100,100,100)
            pixels.show()
            oled.text('White', 0, 0)
            oled.show()
            oled.fill(0)
        elif value == 26:
            while value == 26:
                value = Ir.Getir()
            for i in range(num_leds):
                pixels.set_pixel(i,0,0,0)
            pixels.show()
            oled.text('Black', 0, 0)
            oled.show()
            oled.fill(0)
        value = None

