from gpiozero import Servo
from time import sleep

servo = Servo(7)
position = -1 

# will move the servo from postion -1
# to position 1
while position < 1:
    servo.value = position
    sleep(0.1)
    position += 1
