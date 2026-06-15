from hcsr04 import HCSR04
from machine import Pin, PWM
from time import sleep
from servo import Servo
import dht

ultrassom = HCSR04(trigger_pin=5, echo_pin=18)
dhtSensor = dht.DHT22(Pin(12))
motor = Servo(pin=26)
pushButton = Pin(23, Pin.IN)
buzzer = PWM(Pin(13, Pin.OUT))
led = Pin(15, Pin.OUT)

distanciaAnterior = ultrassom.distance_cm()

def buzz(freq, tempo):
    buzzer.freq(freq)
    buzzer.duty(50)
    sleep(tempo)
    buzzer.duty(0)

while True:
    dhtSensor.measure()
    temperatura = dhtSensor.temperature()

    if temperatura > 45:
        print("Temperatura elevada!")
        buzz(300, 0.2)

    logic_state = pushButton.value()
    
    if logic_state == True:
        print("Portão abrindo!")
        motor.move(90)
        sleep(5)
    else:
        motor.move(180)
        sleep(2)

    distanciaAtual = ultrassom.distance_cm()
    diferenca = abs(distanciaAtual - distanciaAnterior)

    if diferenca >= 10:
        print("Movimento detectado!")
        led.on()
        sleep(5)
    else:
        led.off()

    distanciaAnterior = distanciaAtual

    sleep(1)