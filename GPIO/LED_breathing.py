import RPi.GPIO as GPIO
import time

LED_red = 18

GPIO.setmode(GPIO.BCM)  #use BCM numbers
GPIO.setup(LED_red,GPIO.OUT)    #set  the LED_red OUTPUT MODE
GPIO.output(LED_red,GPIO.LOW)   #make LED_red output LOW level
pwm = GPIO.PWM(18,100) #create PWM instance
pwm.start(0) #start PWM

def brighten(): #define function
    for i in range(0,100,+1):
        pwm.ChangeDutyCycle(i)  #change the frequency, To lighten gradually
        time.sleep(0.01)

def darken():
    for i in range(100,0,-1):
        pwm.ChangeDutyCycle(i)  #To darken gradually
        time.sleep(0.01)

while True: #loop
    brighten()  #call function
    darken()

pwm.stop()  #stop PWM

GPIO.cleanup()  #release all GPIO
