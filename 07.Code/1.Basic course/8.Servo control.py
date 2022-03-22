from pico_car import pico_car

Servo = pico_car()

#180 servo S1 angle 0
#the parameters are (steering gear number, steering gear angle)
Servo.servo180(1,0)
#270 servo
Servo.servo270(2,90)
#360 servo
Servo.servo360(3,360)