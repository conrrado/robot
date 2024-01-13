import RPi.GPIO as GPIO
import time

# GPIO pins setup
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)

# Loop to blink LED
try:
    while True:
        GPIO.output(17, GPIO.HIGH) # turn on LED
        time.sleep(1) # wait 1 second
        GPIO.output(17, GPIO.LOW) # turn off LED
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup() # clean pins setup and quit the program
