from sensorPresenca import SensorPresenca
from servoMotor import ServoMotor
import utime
from machine import Pin

servo = ServoMotor()
sensor_movimento = SensorPresenca()

while True:
    if sensor_movimento.detecta_movimento():
        servo.ativa_servo()
    utime.sleep(0.2)
    
