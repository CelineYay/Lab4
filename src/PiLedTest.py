import hal.hal_input_switch as switch
from hal import hal_led as led
#system import
import socket
import time
from time import sleep

switch.init()

def blink():
    led.init()
    state = int(switch.read_slide_switch())
    while state == 1:
        state = int(switch.read_slide_switch())
        led.set_output(0,1)
        sleep(0,2)
        led.set_output(0, 0)
        sleep(0, 2)
    #led.set_output(24,0) for 2b
    ''' 2c
    while state == 0:
        state = int(switch.read_slide_switch())
        led.set_output(0, 1)
        sleep(0, 1)
        led.set_output(0, 0)
        sleep(0, 1)
    '''
    if state == 0:
        for i in range(3000):
            state = int(switch.read_slide_switch())
            led.set_output(0, 1)
            sleep(0, 1)
            led.set_output(0, 0)
            sleep(0, 1)

blink()
