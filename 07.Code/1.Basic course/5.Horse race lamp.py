import time
from pico_car import ws2812b

num_leds = 8  # Number of NeoPixels
# Pin where NeoPixels are connected
pixels = ws2812b(num_leds, 0)
# Set all led
pixels.fill(10,10,10)
pixels.show()
# horse race lamp
while True:
    for i in range(num_leds):
        for j in range(num_leds):
            #pixel_num, red, green, blue
            pixels.set_pixel(j,abs(i+j)%10,abs(i-(j+3))%10,abs(i-(j+6))%10)
        pixels.show()
        time.sleep(0.05)