import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
led = 26
GPIO.setup(6, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

botton = 6
state = 0
while True:
    GPIO.output(led, not GPIO.input(botton))
       
  
