import RPi.GPIO as GPIO
import time

LED_red = 18
i1 = 0
i2 = 0
i3 = 0

GPIO.setmode(GPIO.BCM)  #use BCM numbers
GPIO.setup(LED_red,GPIO.OUT)    #set the LED_red OUTPUT mode
GPIO.output(LED_red,GPIO.LOW)   #make LED_red output LOW level

while True:
    while(i1<3):
        GPIO.output(LED_red,GPIO.HIGH)  #turn on LED
        time.sleep(0.1)
        GPIO.output(LED_red,GPIO.LOW)   #turn off LED
        time.sleep(0.1)
        print(".")
        i1 += 1

    while(i2<3):
        GPIO.output(LED_red,GPIO.HIGH)  #turn on LED
        time.sleep(1)
        GPIO.output(LED_red,GPIO.LOW)   #turn off LED
        time.sleep(1)
        print("_")
        i2 += 1

    while(i3<3):

        GPIO.output(LED_red,GPIO.HIGH)  #turn on LED
        time.sleep(0.1)
        GPIO.output(LED_red,GPIO.LOW)   #turn off LED
        time.sleep(0.1)
        print(".")
        i3 += 1
    time.sleep(3)
    i1 = 0
    i2 = 0
    i3 = 0

GPIO.cleanup()  #release all GPIO
