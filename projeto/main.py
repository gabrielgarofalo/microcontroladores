from sensorPresenca import SensorPresenca
from servoMotor import ServoMotor
from sensorIR import SensorIR
import utime
from machine import Pin

servo = ServoMotor()
sensor_movimento = SensorPresenca()
ir = SensorIR()

while True:
    ir.detecta_movimento()
    if sensor_movimento.detecta_movimento():
        servo.ativa_servo()
    utime.sleep(0.2)
    

