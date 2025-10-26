from machine import Pin

moteur_in = Pin(15,Pin.OUT)
moteur_out = Pin(26,Pin.OUT)

def start():
    moteur_in.hight()
    moteur_out.low()
    print('moteur demarrer')

def stop():
    moteur_in.low()
    print('moteur arrter')
    