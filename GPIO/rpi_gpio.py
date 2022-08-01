import RPi.GPIO as GPIO
import time

LED_red = 18

GPIO.setmode(GPIO.BCM)  #use BCM numbers
GPIO.setup(LED_red,GPIO.OUT)    #set  the LED_red OUTPUT MODE
GPIO.output(LED_red,GPIO.LOW)   #make LED_red output LOW level

GPIO.cleanup()  #release all GPIO
