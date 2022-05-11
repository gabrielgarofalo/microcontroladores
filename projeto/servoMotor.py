from time import sleep
from machine import Pin, PWM

class ServoMotor:
    
    def __init__(self):
        self.pwm = PWM(Pin(1))
        self.freq = 50
        
    # Gira o servo - (1000 é grau 0 e 9000 é grau 180)
    def ativa_servo(self):
        print(self.freq)
        for position in range(1000, 9000, self.freq):
            self.pwm.duty_u16(position)
            
