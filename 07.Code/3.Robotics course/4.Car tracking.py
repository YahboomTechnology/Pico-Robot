from machine import Pin, I2C
from pico_car import pico_car, ws2812b, SSD1306_I2C
import time

Motor = pico_car()
num_leds = 8  # Number of NeoPixels
# Pin where NeoPixels are connected
pixels = ws2812b(num_leds, 0)
# Set all led off
pixels.fill(0,0,0)
pixels.show()
#initialization oled
i2c=I2C(1, scl=Pin(15),sda=Pin(14), freq=100000)
oled = SSD1306_I2C(128, 32, i2c)
#Define the tracking sensor, 1-4 from left to right
#recognize that black is 0 and white is 1
#Tracing_1 Tracing_2 Tracing_3 Tracing_4
#    2         3        4          5     
Tracing_1 = machine.Pin(2, machine.Pin.IN)
Tracing_2 = machine.Pin(3, machine.Pin.IN)
Tracing_3 = machine.Pin(4, machine.Pin.IN)
Tracing_4 = machine.Pin(5, machine.Pin.IN)

while True:
    
    #四路循迹引脚电平状态
    #Four channel tracking pin level status
    # 0 0 X 0
    # 1 0 X 0
    # 0 1 X 0
    #处理右锐角和右直角的转动
    #Handle the rotation of right acute angle and right right right angle
    if (Tracing_1.value() == 0 or Tracing_2.value() == 0) and Tracing_4.value() == 0:
        Motor.Car_Right(120,120)
        for i in range(num_leds):
            pixels.set_pixel(i,0,255,0)
        oled.text('Turn Right', 0, 0)
        #time.sleep(0.08)
        
    #四路循迹引脚电平状态
    #Four channel tracking pin level status
    # 0 X 0 0       
    # 0 X 0 1 
    # 0 X 1 0       
    #处理左锐角和左直角的转动
    #Handle the rotation of left sharp angle and left right angle
    elif Tracing_1.value() == 0 and (Tracing_3.value() == 0 or Tracing_4.value() == 0):
        Motor.Car_Left(120,120)
        for i in range(num_leds):
            pixels.set_pixel(i,0,0,255)
        oled.text('Turn Left', 0, 0)
        #time.sleep(0.08)
        
    # 0 X X X
    #最左边检测到
    #Leftmost detected
    elif Tracing_1.value() == 0:
        Motor.Car_Left(100,100)
        for i in range(num_leds):
            pixels.set_pixel(i,0,0,255)
        oled.text('Turn Left', 0, 0)
    
    # X X X 0
    #最右边检测到
    #Rightmost detected
    elif Tracing_4.value() == 0:
        Motor.Car_Right(100,100)
        for i in range(num_leds):
            pixels.set_pixel(i,0,255,0)
        oled.text('Turn Right', 0, 0)

    # X 0 1 X
    #处理左小弯
    #Deal with small left bend
    elif Tracing_2.value() == 0 and Tracing_3.value() == 1:
        Motor.Car_Run(0,100)
        for i in range(num_leds):
            pixels.set_pixel(i,0,0,255)
        oled.text('Left', 0, 0)

    # X 1 0 X  
    #处理右小弯
    #Handle small right bend
    elif Tracing_2.value() == 1 and Tracing_3.value() == 0:
        Motor.Car_Run(100,0)
        for i in range(num_leds):
            pixels.set_pixel(i,0,255,0)
        oled.text('Right', 0, 0)

    # X 0 0 X
    #处理直线
    #Processing line
    elif Tracing_2.value() == 0 and Tracing_3.value() == 0:
        Motor.Car_Run(200,200)
        for i in range(num_leds):
            pixels.set_pixel(i,255,255,255)
        oled.text('Run', 0, 0)
        
    pixels.show()
    oled.show()
    oled.fill(0)
#其他时小车保持上一个小车运行状态
#In other cases, the trolley keeps the previous trolley running
