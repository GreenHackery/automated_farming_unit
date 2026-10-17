from machine import Pin
import time, json

float_sw = Pin(15, Pin.IN, Pin.PULL_UP)
beam = Pin(16, Pin.IN, Pin.PULL_UP)

def send(name, type_, value):
    print(json.dumps({"name": name, "type": type_, "value": value}))

while True:
    send("tank_float_1", "float_switch", float_sw.value())
    send("beam_1", "beam_break", beam.value())
    time.sleep(0.5)