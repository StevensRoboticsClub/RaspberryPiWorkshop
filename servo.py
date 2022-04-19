
import RPi.GPIO as GPIO
from gpiozero import Servo
from time import sleep

GPIO.setmode(GPIO.BOARD)

PIN_SERVO = 7
GPIO.setup(PIN_SERVO, GPIO.OUT)

servo = Servo(PIN_SERVO)
position = -1 

# will move the servo from postion -1
# to position 1
while position < 1:
    servo.value = position
    sleep(0.1)
    position += 1 
    
