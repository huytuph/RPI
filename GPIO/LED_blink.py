import RPi.GPIO as GPIO
import time

led_red = 18

GPIO.setmode(GPIO.BCM) #use BCM numbers
GPIO.setup(led_red,GPIO.OUT) #set the led_red OUTPUT mode
GPIO.output(led_red,GPIO.LOW) #make led_red LOW level
 
while True:
    GPIO.output(led_red,GPIO.HIGH) #turn on led_red
    print("Red LED is ON")
    time.sleep(1)
    GPIO.output(led_red,GPIO.LOW) #turn off led_red
    print("Red LED is OFF")
    time.sleep(1)
 
GPIO.cleanup() #release all GPIO
