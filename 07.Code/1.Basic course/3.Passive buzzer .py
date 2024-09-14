from machine import Pin, PWM
import time
# set buzzer pin
BZ = PWM(Pin(22))
BZ.freq(1000)
# Initialize music
CM = [0, 330, 350, 393, 441, 495, 556, 624] 
song = [CM[1],CM[1],CM[5],CM[5],CM[6],CM[6],CM[5],CM[4],CM[4],CM[3],CM[3],CM[2],CM[2],CM[1],]
beat = [ 0.5,0.5,0.5,0.5,0.5,0.5,1,0.5,0.5,0.5,0.5,0.5,0.5,1,]
# music   
def music():
        print('Playing song ...')
        for i in range(len(song)):
            BZ.duty_u16(500)
            BZ.freq(song[i])
            time.sleep(beat[i]) 
            BZ.duty_u16(0)
            time.sleep(0.01) 
# play music   
music()
print("Ending")


