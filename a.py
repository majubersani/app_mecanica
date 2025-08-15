# importar bibliotecas
# quem sera utilizado
import time

from nec import NEC_16

from hcsr04 import HCSR04
import utime
from time import sleep
from machine import Pin, ADC, time_pulse_us, PWM, SoftI2C
import time
from machine import Pin, I2C
import ssd1306
import dht
from nec import NEC_16

# configuracao
# onde estao os itens/componentes

# luz
led1 = Pin(25, Pin.OUT)

# led ultrassonico:
led2 = Pin(32, Pin.OUT)
led3 = Pin(33, Pin.OUT)

# portas outro ultrassônico:
TRIG = Pin(4)
ECHO = Pin(2)

# Parametros configuraçao
# Cria objeto sonic do tipo HCSR04
sonic = HCSR04(trigger_pin=TRIG, echo_pin=ECHO)

# servo
servo_motor = PWM(Pin(23, mode=Pin.OUT))
servo_motor.freq(50)  # Padrao

# Oled:
i2c = I2C(0, scl=Pin(22), sda=Pin(21))
oled_width = 128
oled_height = 64
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

# temperatura(DHT22)
sensor_pin = 12
sensor = dht.DHT22(sensor_pin)

"""
 [_]
 |||
 123
1 sinal
2 GND
3 VCC
"""
ir_data = 0
led = 0
porta = 0
ledluz = 0
cm = 0

global valor_vetor
valor_vetor = 0

global valor_data


def callback(data, addr, ctrl):
    global ir_data
    if data > 0:
        # print(f"Num_botao {data:02x} cod {addr:04x} ft {ir_key[data]}")
        print(f"Num_botao {data:02x} cod {data}")
        ir_data = data


def fechar_vetor():
    oled.fill(0)
    global valor_vetor
    valor_vetor = not (valor_vetor)
    oled.fill(0)
    oled.text(f"fechar", 10, 10)
    oled.show()
    oled.text(f"cortina", 20, 20)
    oled.show()
    time.sleep(0.5)
    servo_motor.duty(25)
    time.sleep(0.5)


def abrir_vetor():
    oled.fill(0)
    global valor_vetor
    valor_vetor = not (valor_vetor)
    oled.fill(0)
    oled.text(f"abrir", 10, 10)
    oled.show()
    oled.text(f"cortina", 20, 20)
    oled.show()
    time.sleep(0.5)
    servo_motor.duty(126)
    time.sleep(0.5)

ir = NEC_16(Pin(34, Pin.IN), callback)

# programa
# o que / como ira acontecer
while True:
    # programa temp:
    sensor.measure()
    sensor.temperature()
    sensor.humidity()

    # programa ultra:
    cm = sonic.distance_cm()

    if ir_data > 0:
        # luz
        if ir_data == 24:
            print("Tecla 2")
            print("Luz")
            if led == 0:
                oled.fill(0)
                led = not (led)
                oled.fill(0)
                oled.text(f"Luz", 10, 10)
                oled.show()
                oled.text(f"ligada", 20, 20)
                oled.show()
                led1.on()
                led = 1
                print("Luz ligada")
            else:
                oled.fill(0)
                led = not (led)
                oled.fill(0)
                oled.text(f"Luz", 10, 10)
                oled.show()
                oled.text(f"desligada", 20, 20)
                oled.show()
                led1.off()
                led = 0
                print("luz desligada")

        # temperatura
        elif ir_data == 48:
            print("Tecla 1")
            print(sensor.temperature())
            print(sensor.humidity())
            time.sleep(0.1)
            oled.fill(0)
            oled.text(f"temperatura, ", 10, 10)
            oled.show()
            oled.text(f"{sensor.temperature()}", 20, 20)
            oled.show()
            oled.text
            oled.show()


        # distancia
        elif ir_data == 122:
            print("Tecla 3")
            print(f'teste: {cm}')
            if cm <= 100:
                cm = not (cm)
                oled.fill(0)
                oled.text(f"Centimetros", 10, 10)
                oled.show()
                oled.text(f"menor que 100", 20, 20)
                oled.show()
                led2.off()
                led3.on()
                print("Distancia em centimetros é", cm, "proximidade alta, alerta")
            elif cm > 100:
                cm = not (cm)
                oled.fill(0)
                oled.text(f"Centimetros", 10, 10)
                oled.show()
                oled.text(f"maior que 100", 20, 20)
                oled.show()
                led3.off()
                led2.on()
                print("Distancia em Centimetros é", cm, "proximidade estável")

                time.sleep(0.05)

        # porta
        elif ir_data == 16:
            print("Tecla 4")
            if porta == 0:
                porta = 1
                oled.fill(0)
                oled.text('Porta foi', 10, 10)
                oled.text('destrancada!', 10, 20)
                oled.show()
                oled.fill(0)
            elif porta == 1:
                porta = 0
                oled.fill(0)
                oled.text('Porta foi', 10, 10)
                oled.text('trancada!', 10, 20)
                oled.show()
                oled.fill(0)
                time.sleep(0.1)


        # servo
        elif ir_data == 56:
            print("Tecla 5")
            if valor_vetor == 1:
                abrir_vetor()
                valor_vetor = 0

            else:
                fechar_vetor()
                valor_vetor = 1
                time.sleep(0.1)

        # muisca
    elif ir_data == 66:
        print("Tecla 7")
        oled.text('HINO PALMEIRAS', 2, 20)
        oled.text('by Palmeiras', 2, 30)
        oled.show()
        oled.fill(0)
        time.sleep(2)
        oled.text('quando surge', 1, 10)
        oled.text('o alviverde', 2, 20)
        oled.text('imponente', 2, 30)
        oled.show()
        oled.fill(0)
        time.sleep(3)
        oled.text('no gramado', 2, 10)
        oled.text('em que a luta', 2, 20)
        oled.text('o aguarda', 2, 30)
        oled.show()
        oled.fill(0)
        time.sleep(3)
        oled.text('sabe bem o que', 2, 10)
        oled.text('vem pela frente', 2, 20)
        oled.text('que a dureza do', 2, 30)
        oled.text('prelio nao tarda', 2, 40)
        oled.show()
        oled.fill(0)
        time.sleep(3)
        oled.text('e o palmeiras', 2, 10)
        oled.text('no ardor da par', 2, 20)
        oled.text('tida tranformando', 1, 30)
        oled.text('a lealdade em ', 2, 40)
        oled.text('padrao', 2, 50)
        oled.show()
        oled.fill(0)
        time.sleep(3)
        oled.text('sabe sempre levar', 2, 10)
        oled.text('de vencida e', 2, 20)
        oled.text('mostrar que de', 2, 30)
        oled.text('fato e campeao', 2, 40)
        oled.show()
        oled.fill(0)
        time.sleep(3)

    else:
        print("nao cadastrado")
    ir_data = 0