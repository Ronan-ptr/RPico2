## IMPORT Modules et Fonctions
from machine import Pin
import time

## DEFINITION des Objets
led=Pin(15, Pin.OUT) # Entrée LED Pin 15
btn=Pin(13, Pin.IN) # Sortie Boutton Pin 13

## MISE EN PLACE Variables
#btn_on=0 # Lire la valeur du bouton

#off=led.value(0) # LED off
#on=led.value(1) # LED on

## CREATION Fonctions
def push() :
    if btn.value()==1 : # Verifie si valeur bouton=1
        led.value(0) # LED off
        #led.toggle() # Change etat LED
    else :
        led.value(1)
    
## PROGRAMME
while True :
    push()
    time.sleep(0.01)