import time
from machine import Pin, I2C, PWM, Timer, UART, ADC
from pico_car import SSD1306_I2C, pico_car, ws2812b, ultrasonic

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
#initialization Bluetooth
uart = UART(0, 9600, bits=8, parity=None, stop=1, tx=Pin(16), rx=Pin(17))
dat = 0
#initialization ADC
Quantity_of_electricity = machine.ADC(28)
Sound = machine.ADC(27)
#define Timer
tim = Timer()
def tick(timer):
    w_power = int(Quantity_of_electricity.read_u16()/65535*240)
    if w_power > 100:
        w_power = 100
    w_distance = ultrasonic.Distance_accurate()
    w_sounds = int(Sound.read_u16()/65535*200)
    uart.write('$DAT')
    uart.write(str(w_distance))
    uart.write(',')
    uart.write(str(w_sounds))
    uart.write(',')
    uart.write(str(w_power))
    uart.write('#')
#set timer frequency 0.5
tim.init(freq = 0.5,mode = Timer.PERIODIC,callback = tick)

#define water lamp
def water():
    global i,dat
    i = 0
    while dat != b'M#':
        while uart.any() > 0:
            dat = uart.read(2)
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
        time.sleep(0.1)
    i = 0

#define breathing lamp
def breathing():
    global i,dat
    i = 0
    brightness = 0
    fadeAmount = 1
    while dat != b'M#':
        while uart.any() > 0:
            dat = uart.read(2)
        for i in range(num_leds):
            pixels.set_pixel(i,0,brightness,brightness)
        pixels.show()
        brightness = brightness + fadeAmount
        if brightness <= 0 or brightness >= 200:
            fadeAmount = -fadeAmount
        time.sleep(0.005)
    i = 0

#define horse lamp
def horse():
    global dat
    while dat != b'M#':
        while uart.any() > 0:
            dat = uart.read(2)
        for i in range(num_leds):
            for j in range(num_leds):
                #pixel_num, red, green, blue
                pixels.set_pixel(j,abs(i+j)%10,abs(i-(j+3))%10,abs(i-(j+6))%10)
            pixels.show()
            time.sleep(0.05)

#Define the tracking sensor, 1-4 from left to right
#recognize that black is 0 and white is 1
#Tracing_1 Tracing_2 Tracing_3 Tracing_4
#    2         3        4          5     
Tracing_1 = machine.Pin(2, machine.Pin.IN)
Tracing_2 = machine.Pin(3, machine.Pin.IN)
Tracing_3 = machine.Pin(4, machine.Pin.IN)
Tracing_4 = machine.Pin(5, machine.Pin.IN)
#define line
def line():
    global dat
    oled.fill(0)
    while dat != b'V#':
        while uart.any() > 0:
            dat = uart.read(2)
            
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
    pixels.fill(0,0,0)
    Motor.Car_Stop()
    BZ.duty_u16(0)

#define ultrasonic avoid    
def avoid():
    global dat
    oled.fill(0)
    while dat != b'V#':
        while uart.any() > 0:
            dat = uart.read(2)
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
    pixels.fill(0,0,0)
    Motor.Car_Stop()
    BZ.duty_u16(0)

#define ultrasonic voice    
def voice():
    global dat
    oled.fill(0)
    while dat != b'V#':
        while uart.any() > 0:
            dat = uart.read(2)
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
    pixels.fill(0,0,0)
    Motor.Car_Stop()
    BZ.duty_u16(0)

while True:
    #receive data
    while uart.any() > 0:
        dat = uart.read(2)
        #OLED display
        if dat == b'X#':
            for oledi in range(128):
                for oledj in range(10):
                    oled.pixel(oledi, oledj,0)
            datoled_1 = uart.read(16)
            stroled_1 = str(datoled_1)
            stroled_1 = stroled_1.replace("b'", "")
            stroled_1 = stroled_1.replace("'", "")
            stroled_1 = stroled_1.replace("$", "")
            oled.text(stroled_1, 0, 0)
            oled.show()
            print(stroled_1)
        elif dat == b'Y#':
            for oledi in range(128):
                for oledj in range(10,20):
                    oled.pixel(oledi, oledj,0)
            datoled_2 = uart.read(16)
            stroled_2 = str(datoled_2)
            stroled_2 = stroled_2.replace("b'", "")
            stroled_2 = stroled_2.replace("'", "")
            stroled_2 = stroled_2.replace("$", "")
            oled.text(stroled_2, 0, 10)
            oled.show()
            print(stroled_2)
        elif dat == b'Z#':
            for oledi in range(128):
                for oledj in range(20,30):
                    oled.pixel(oledi, oledj,0)
            datoled_3 = uart.read(16)
            stroled_3 = str(datoled_3)
            stroled_3 = stroled_3.replace("b'", "")
            stroled_3 = stroled_3.replace("'", "")
            stroled_3 = stroled_3.replace("$", "")
            oled.text(stroled_3, 0, 20)
            oled.show()
            print(stroled_3)
        elif dat == b'W#':
            BBuzzer = uart.read(1)
            if BBuzzer == b'1':
                BZ.duty_u16(500)
                BZ.freq(277)
            elif BBuzzer == b'2':
                BZ.duty_u16(500)
                BZ.freq(311)
            elif BBuzzer == b'3':
                BZ.duty_u16(500)
                BZ.freq(370)
            elif BBuzzer == b'4':
                BZ.duty_u16(500)
                BZ.freq(415)
            elif BBuzzer == b'5':
                BZ.duty_u16(500)
                BZ.freq(466)

    #car control
    if dat == b'A#':
        Motor.Car_Run(255,255)
    elif dat == b'B#':
        Motor.Car_Back(255,255)
    elif dat == b'C#':
        Motor.Car_Run(0,255)
    elif dat == b'D#':
        Motor.Car_Run(255,0)
    elif dat == b'E#':
        Motor.Car_Left(255,255)
    elif dat == b'F#':
        Motor.Car_Right(255,255)
    elif dat == b'0#':
        Motor.Car_Stop()
    #music control
    elif dat == b'1#':
        BZ.duty_u16(500)
        BZ.freq(262)
    elif dat == b'2#':
        BZ.duty_u16(500)
        BZ.freq(294)
    elif dat == b'3#':
        BZ.duty_u16(500)
        BZ.freq(330)
    elif dat == b'4#':
        BZ.duty_u16(500)
        BZ.freq(349)
    elif dat == b'5#':
        BZ.duty_u16(500)
        BZ.freq(392)
    elif dat == b'6#':
        BZ.duty_u16(500)
        BZ.freq(440)
    elif dat == b'7#':
        BZ.duty_u16(500)
        BZ.freq(494)
    elif dat == b'8#':
        BZ.duty_u16(500)
        BZ.freq(523)
    elif dat == b'O#':
        BZ.duty_u16(0)
    #car light
    elif dat == b'G#':
        pixels.fill(255,0,0)
        pixels.show()
    elif dat == b'H#':
        pixels.fill(0,255,0)
        pixels.show()
    elif dat == b'I#':
        pixels.fill(0,0,255)
        pixels.show()
    elif dat == b'J#':
        pixels.fill(255,255,0)
        pixels.show()
    elif dat == b'K#':
        pixels.fill(0,255,255)
        pixels.show()
    elif dat == b'L#':
        pixels.fill(255,0,255)
        pixels.show()
    elif dat == b'N#':
        water()
    elif dat == b'P#':
        horse()
    elif dat == b'Q#':
        breathing()
    elif dat == b'M#':
        pixels.fill(0,0,0)
        pixels.show()
        i = 0
        brightness = 0
        fadeAmount = 1
    #mode
    elif dat == b'S#':
        line()
    elif dat == b'T#':
        avoid()
    elif dat == b'U#':
        voice()
    elif dat == b'V#':
        oled.fill(0)
        oled.show()
        pixels.fill(0,0,0)
        pixels.show()
        Motor.Car_Stop()
        BZ.duty_u16(0)
    time.sleep(0.01)
