from machine import Pin
import utime

class SensorPresenca():
    
    def __init__(self):
        self.entrada = Pin(16, Pin.IN, Pin.PULL_UP)
        
    # Função pra detectar movimento
    def detecta_movimento(self):
        if self.entrada.value() == 0:
            print("Movimento Detectado!")
            #self.saida.high()
            return True
        else:
            print("Esperando movimento...")
            #self.saida.low()
            return False
            
        
        


