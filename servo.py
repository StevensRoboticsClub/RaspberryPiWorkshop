
import RPi.GPIO as GPIO
from gpiozero import Servo
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(25, GPIO.OUT)

servo = Servo(25)
position = -1 

# will move the servo from postion -1
# to position 1
while position < 1:
    servo.value = position
    sleep(0.1)
    position += 1 
    
