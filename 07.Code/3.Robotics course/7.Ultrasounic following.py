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
song = [CM[1],CM[1],CM[5],CM[5],CM[6],CM[6],CM[5],CM[4],CM[4],CM[3],CM[3],CM[2],CM[2],CM[1],]
beat = [ 0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,0.5,0.5,1,]
#initialization ultrasonic
ultrasonic = ultrasonic()
#initialization oled
i2c=I2C(1, scl=Pin(15),sda=Pin(14), freq=100000)
oled = SSD1306_I2C(128, 32, i2c)
#Define variables
global time_ul, music_i, t_turn, i_turn, t_turn, music_back
music_i = 0
time_ul = 0
i_run = 0
i_turn = 0
t_turn = 0
music_back = 0

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
    if distance < 9:
        for i in range(num_leds):
            pixels.set_pixel(i,255,0,0)
        pixels.show()
        Motor.Car_Back(100,100)
        if music_back < 5:
            BZ.duty_u16(500)
            BZ.freq(624)
        else:
            BZ.duty_u16(0)
    elif distance >= 9 and distance < 20:
        if i_run == 0:
            pixels.set_pixel(6,0,0,0)
            pixels.set_pixel(7,0,0,0)
            pixels.set_pixel(2,150,0,150)
            pixels.set_pixel(3,150,0,150)
            i_run = 1
        elif i_run == 1:
            pixels.set_pixel(2,0,0,0)
            pixels.set_pixel(3,0,0,0)
            pixels.set_pixel(1,150,0,150)
            pixels.set_pixel(4,150,0,150)
            i_run = 2
        elif i_run == 2:
            pixels.set_pixel(1,0,0,0)
            pixels.set_pixel(4,0,0,0)
            pixels.set_pixel(0,150,0,150)
            pixels.set_pixel(5,150,0,150)
            i_run = 3
        elif i_run == 3:
            pixels.set_pixel(0,0,0,0)
            pixels.set_pixel(5,0,0,0)
            pixels.set_pixel(6,150,0,150)
            pixels.set_pixel(7,150,0,150)
            i_run = 4
        elif i_run == 4:
            pixels.set_pixel(0,0,0,0)
            pixels.set_pixel(5,0,0,0)
            pixels.set_pixel(6,150,0,150)
            pixels.set_pixel(7,150,0,150)
            i_run = 0
        pixels.show()
        Motor.Car_Run(100,100)
        BZ.duty_u16(500)
        BZ.freq(song[music_i])
        time.sleep(beat[music_i]/2)
        BZ.duty_u16(0)  
            
    else:
        BZ.duty_u16(0)
        if i_turn == 0:
            pixels.set_pixel(7,0,0,0)
            pixels.set_pixel(0,0,150,150)
        else:
            pixels.set_pixel(i_turn-1,0,0,0)
            pixels.set_pixel(i_turn,0,150,150)
        pixels.show()
        if t_turn < 5:
            Motor.Car_Right(120,120)
        elif t_turn >= 5 and t_turn < 10:
            Motor.Car_Left(120,120)
          
    time_ul = time_ul + 1
    music_i = music_i + 1
    if music_i >= len(song):
        music_i = 0
    i_turn = i_turn + 1
    if i_turn == 8:
        i_turn = 0
    t_turn = t_turn + 1
    if t_turn >= 10:
        t_turn = 0
    music_back = music_back + 1
    if music_back >= 10:
        music_back = 0
    time.sleep(0.01)
