from utime import sleep
from machine import Pin, PWM

class ServoMotor:
    
    def __init__(self, pin: int):
        self.freq = 50
        self.pwm = PWM(Pin(pin))
        self.pwm.freq(self.freq)
        
        
    # Gira o servo - (1000 é grau 0 e 9000 é grau 180)
    def ativa_servo(self):
        print("Roda Motor")
        for position in range(200, 6500, self.freq):
            self.pwm.duty_u16(position)
            sleep(0.1)
            

