from pico_car import pico_car, ws2812b
import time
from machine import Pin, PWM

Motor = pico_car()
# set buzzer pin
BZ = PWM(Pin(22))
BZ.freq(1000)
num_leds = 8  # Number of NeoPixels
# Pin where NeoPixels are connected
pixels = ws2812b(num_leds, 0)
# Set all led off
pixels.fill(0,0,0)
pixels.show()
# Initialize music
CM = [0, 330, 350, 393, 441, 495, 556, 624] 
song = [CM[1],CM[1],CM[5],CM[5],CM[6],CM[6],CM[5],
        CM[4],CM[4],CM[3],CM[3],CM[2],CM[2],CM[1],]
beat = [ 0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,0.5,0.5,1,]
# music   
def music_Run():
    for i in range(0,2):
        BZ.duty_u16(500)
        BZ.freq(song[i])
        time.sleep(beat[i]) 
        BZ.duty_u16(0)
        time.sleep(0.01)  
def music_Back():
    for i in range(2,4):
        BZ.duty_u16(500)
        BZ.freq(song[i])
        time.sleep(beat[i]) 
        BZ.duty_u16(0)
        time.sleep(0.01)  
def music_Left():
    for i in range(4,7):
        BZ.duty_u16(500)
        BZ.freq(song[i])
        time.sleep(beat[i]) 
        BZ.duty_u16(0)
        time.sleep(0.01) 
def music_Right():
    for i in range(7,9):
        BZ.duty_u16(500)
        BZ.freq(song[i])
        time.sleep(beat[i]) 
        BZ.duty_u16(0)
        time.sleep(0.01) 
def music_TLeft():
    for i in range(9,11):
        BZ.duty_u16(500)
        BZ.freq(song[i])
        time.sleep(beat[i]) 
        BZ.duty_u16(0)
        time.sleep(0.01) 
def music_TRight():
    for i in range(11,14):
        BZ.duty_u16(500)
        BZ.freq(song[i])
        time.sleep(beat[i]) 
        BZ.duty_u16(0)
        time.sleep(0.01) 
#Car forward
Motor.Car_Run(255,255)
for i in range(num_leds):
    pixels.set_pixel(i,255,255,0)
pixels.show()
music_Run()
#Car back
Motor.Car_Back(255,255)
for i in range(num_leds):
    pixels.set_pixel(i,0,255,255)
pixels.show()
music_Back()
#left
Motor.Car_Run(0,255)
for i in range(num_leds):
    pixels.set_pixel(i,255,0,255)
pixels.show()
music_Left()
#right
Motor.Car_Run(255,0)
for i in range(num_leds):
    pixels.set_pixel(i,255,0,0)
pixels.show()
music_Right()
#Turn left
Motor.Car_Left(255,255)
for i in range(num_leds):
    pixels.set_pixel(i,0,255,0)
pixels.show()
music_TLeft()
#Turn right
Motor.Car_Right(255,255)
for i in range(num_leds):
    pixels.set_pixel(i,0,0,255)
pixels.show()
music_TRight()
#Car stop
Motor.Car_Stop()
for i in range(num_leds):
    pixels.set_pixel(i,0,0,0)
pixels.show()
