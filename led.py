import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)

# Will turn on LED, wait 3 seconds,
# then turn it off
print("On")
GPIO.output(17,GPIO.HIGH)
time.sleep(3)

print("Off")
GPIO.output(17,GPIO.LOW)

GPIO.cleanup()