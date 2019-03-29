#!/usr/local/bin/python

__author__ = 'Gus (Adapted from Adafruit); Malik (Added LED & Light Value Condition Statements)'
__license__ = "GPL"
__maintainer__ = "pimylifeup.com"

import RPi.GPIO as GPIO
import time

# GPIO setwarnings Suppresses the GPIO warnings. 
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

#defines the pins that goes to the circuit
pin_to_circuit = 7
pin = 24  #Red LED
pin2 = 11 #Blue LED
pin3 = 26 #Green LED

# Function: def rc_time(pin_to_circuit)
# Description: This function displays the photoresistor's values by using the 'count' variable,
#           and sets the led to flash either red, green, or blue depending on the values given.
def rc_time(pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.2)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1
        
    # Set's up the GPIO pins for the LEDS
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setup(pin2, GPIO.OUT)
    GPIO.setup(pin3, GPIO.OUT)
    # HIGH stands for ON.
    # LOW  stands for OFF.
    
    # Creates a Loop for Bright to Dim Lighting.
    for i in range (count > 0 and count < 4000):
        GPIO.output(pin3, GPIO.HIGH)
        
        # Turns off the following LEDS in case they were on in a previous run.
        GPIO.output(pin, GPIO.LOW) #Red LED
        GPIO.output(pin2, GPIO.LOW) #Blue LED
  
    # Creates a Loop for Dim to almost Dark Lighting.
    for i in range (count > 4001 and count < 22000):
        GPIO.output(pin2, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(pin2, GPIO.LOW)   
        time.sleep(0.5)
        
        # Turns off the following LEDS.
        GPIO.output(pin3, GPIO.LOW) #Green LED
        GPIO.output(pin, GPIO.LOW) #Red LED
    
    # Creates a Loop for Dark Lightint to almost No Light.
    for i in range (count > 30000 and count < 3800000):
        GPIO.output(pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(pin, GPIO.LOW)   
        time.sleep(0.5)
        
        # Turns off the following LEDS.
        GPIO.output(pin2, GPIO.LOW) #Blue LED
        GPIO.output(pin3, GPIO.LOW) #Green LED
    
    # Prints the count value (also the value for how much light the photoresistor is reading).
    print (count)
    
    # Returns the count value.
    return count
    
    

#Catch when script is interrupted, cleanup correctly
try:
    #Main loop
    while True:
        # print rc_time(pin_to_circuit)
        # Removed the print function call from 'print rc_time(pin_to_circuit) for python3 users.
        # For non-python3 users. Type: sudo python3 'insertFileName.py'. Or use: print rc_time(pin_to_circuit)
        rc_time(pin_to_circuit)
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
