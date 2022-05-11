from time import sleep
from machine import Pin, PWM

class ServoMotor:
    
    def __init__(self, freq):
        self.pwm = PWM(Pin(1))
        self.pwm.freq = freq

    # Gira o servo - (1000 é grau 0 e 9000 é grau 180)
    def ativa_servo(self):
        for position in range(1000, 9000, self.pwm.freq):
            pwm.duty_u16(position)
