from pico_car import pico_car
import time

Motor = pico_car()

#Car forward，parameter(Left motor speed，Right motor speed),speed 0-255
Motor.Car_Run(255,255)
time.sleep(1)
#Car stop
Motor.Car_Stop()