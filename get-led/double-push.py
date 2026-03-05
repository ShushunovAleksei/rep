import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [16, 12, 25, 17, 27, 23, 22, 24]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

up_button = 9
down_button = 10
GPIO.setup(up_button, GPIO.IN)
GPIO.setup(down_button, GPIO.IN)

num = 0
sleep_time = 0.2

def dec2bin(val):
    return [int(element) for element in bin(val)[2:].zfill(8)]

while True:

    if GPIO.input(up_button) and GPIO.input(down_button):
        num = 255
    else:
        if GPIO.input(up_button):
            if num == 255:
                num = 0
            else:
                num += 1
            print(num, dec2bin(num))
            time.sleep(sleep_time)

        if GPIO.input(down_button):
            if num == 0:
                num = 255
            else:
                num -= 1
            print(num, dec2bin(num))
            time.sleep(sleep_time)

    GPIO.output(leds, dec2bin(num))