from machine import Pin
import utime

class SensorPresenca():
    
    def __init__(self):
        self.entrada = Pin(16, Pin.IN, Pin.PULL_UP)
        
    # Função pra detectar movimento
    def detecta_movimento(self):
        if self.entrada.value() == 0:
            print("Movimento Detectado!(MOV)")
            #self.saida.high()
            return True
        else:
            print("Esperando movimento...(MOV)")
            #self.saida.low()
            return False
            
        
        


