from machine import Pin
import utime

led = Pin(16, Pin.OUT)
sensor = Pin(15, Pin.IN)
led.value(0)
#utime.sleep(5)
while True:
    if sensor.value() == 1:
        led.value(0)
    else:
        led.value(1)
    #utime.sleep(1)
    print(sensor.value())
    utime.sleep(0.1)
    
        
# https://www.youngwonks.com/blog/How-to-use-an-infrared-sensor-with-the-Raspberry-Pi-Pico
