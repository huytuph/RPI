from PiicoDev_RFID import PiicoDev_RFID
from PiicoDev_Unified import sleep_ms
from gpiozero import LED
from time import sleep

led_green = LED(23)
led_red = LED(24)

rfid = PiicoDev_RFID() # Initialise the RFID module
auth0 = "Access denied"
auth1 = "Access granted"
print("Place tag near the PiicoDev RFID Module")
while True:    
    if rfid.tagPresent(): # if an RFID tag is present
        id = rfid.readID() # get the id
#        id = rfid.readID(detail=True) # gets more details eg. tag type
        led_red.off()
        led_green.on()
        print(auth1) # print the id
    elif id == ("04:0C:78:FA:12:72:80"):
        print(auth0)
    else:
        led_green.off()
        led_red.on()
        continue

#    sleep_ms(100)
