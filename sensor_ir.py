from machine import Pin
import utime
     print(sensor.value())
    if sensor.value() == 1:
        led.value(0)
    else:
        led.value(1)
        
# https://www.youngwonks.com/blog/How-to-use-an-infrared-sensor-with-the-Raspberry-Pi-Pico