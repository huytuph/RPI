import RPi.GPIO as GPIO
from time import sleep

#LED pin
LED_red = 18
LED_yellow = 23
LED_green = 24

GPIO.setmode(GPIO.BCM)  #use BCM numbers
GPIO.setup(LED_red,GPIO.OUT)    #set the LED_red OUTPUT MODE
GPIO.setup(LED_yellow,GPIO.OUT)    #set the LED_yellow OUTPUT MODE
GPIO.setup(LED_green,GPIO.OUT)    #set the LED_green OUTPUT MODE

GPIO.output(LED_red,GPIO.LOW)   #make LED_red output LOW level
GPIO.output(LED_yellow,GPIO.LOW)   #make LED_yellow output LOW level
GPIO.output(LED_green,GPIO.LOW)   #make LED_green output LOW level

while True:
    GPIO.output(LED_red,GPIO.HIGH)  #turn on LED_red
    sleep(5)
    GPIO.output(LED_red,GPIO.LOW)   #turn off LED_red

    GPIO.output(LED_yellow,GPIO.HIGH)   #turn on LED_yellow
    sleep(0.5)
    GPIO.output(LED_yellow,GPIO.LOW)    #turn off LED_yellow
    sleep(0.5)
    GPIO.output(LED_yellow,GPIO.HIGH)
    sleep(0.5)
    GPIO.output(LED_yellow,GPIO.LOW)
    sleep(0.5)
    GPIO.output(LED_yellow,GPIO.HIGH)
    sleep(0.5)
    GPIO.output(LED_yellow,GPIO.LOW)
    sleep(0.5)

    GPIO.output(LED_green,GPIO.HIGH)    #turn on LED_green
    sleep(5)    #delay 5 seconds
    GPIO.output(LED_green,GPIO.LOW)    #turn off LED_green

GPIO.cleanup()  #release all GPIO
