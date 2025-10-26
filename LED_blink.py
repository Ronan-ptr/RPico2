from machine import Pin, Timer #Vas dans le module "machine" et importe les classes "Pin" et "Timer"

## CREATION DES OBJETS

# LED : Pin25 = led rpico
led = Pin(25, Pin.OUT) # Affecte Pin n°25, mode sortie, a variable "led"
#led.value(1) # LED = on
#led.value(0) # LED = off
#led.toggle() # LED = change etat

# CHRONOMETRE : Timer()
timer = Timer() # Affecte objet Timer(), sans argument, pour mesurer le temps
# Pas arguments = Timer() par défaut :
# Timer(mode=ONE_SHOT, tick_hz=1000000, period=0)


## CREATON DE FONCTION

# CLIGNOTEMENT
def blink(timer): # C
    led.toggle()
    print('Changement etat LED')
    
## CONFIGURATON OBJETS
    
timer.init(freq = 1,
           mode = Timer.PERIODIC,
           callback = blink)