from machine import Pin
import utime

class SensorIR:

    def __init__(self):
        self.sensor = Pin(15, Pin.IN)

    # Função pra detectar movimento
    def detecta_movimento(self):
        if self.sensor.value() != 1:
            print("Movimento Detectado (IR)!")
            #self.saida.high()
            return True
        else:
            print("Esperando movimento...(IR)")
            #self.saida.low()
            return False

