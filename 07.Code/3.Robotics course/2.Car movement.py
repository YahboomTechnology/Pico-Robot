from pico_car import pico_car
import time

Motor = pico_car()

#Car forward，parameter(Left motor speed，Right motor speed),speed 0-255
Motor.Car_Run(255,255)
time.sleep(1)
#Car back
Motor.Car_Back(255,255)
time.sleep(1)
#left
Motor.Car_Run(0,255)
time.sleep(1)
#right
Motor.Car_Run(255,0)
time.sleep(1)
#Turn left
Motor.Car_Left(255,255)
time.sleep(1)
#Turn right
Motor.Car_Right(255,255)
time.sleep(1)
#Car stop
Motor.Car_Stop()