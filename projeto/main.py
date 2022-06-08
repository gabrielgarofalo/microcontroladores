from sensorPresenca import SensorPresenca
from servoMotor import ServoMotor
from sensorIR import SensorIR
import utime
from machine import Pin

print("Ola SIstemsa")

servo_ir = ServoMotor(pin=19)
servo_movimento = ServoMotor(pin=0)
sensor_movimento = SensorPresenca()
ir = SensorIR()
alimentar_agora = Pin(13, Pin.IN)

while True:
    if ir.detecta_movimento():
        servo_ir.ativa_servo()
    if sensor_movimento.detecta_movimento() or alimentar_agora.value() == 1:
        servo_movimento.ativa_servo()
    utime.sleep(0.2)
    
