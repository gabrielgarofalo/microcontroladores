from sensorPresenca import SensorPresenca
from servoMotor import ServoMotor

servo = ServoMotor(50)
sensor_movimento = SensorPresenca()

while True:
    if sensor_movimento.detecta_movimento():
        servo.stiva_servo
