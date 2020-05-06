from time import sleep

import RPi.GPIO as GPIO

PWR_LED = 35


def pwr_led_off():
    GPIO.setup(PWR_LED, GPIO.OUT, initial=GPIO.LOW)


def pwr_led_on():
    GPIO.setup(PWR_LED, GPIO.IN)


def blinking_led():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    pwr_led_on()
    sleep(1)
    pwr_led_off()
    sleep(1)
    pwr_led_on()
    pwr_led_off()
    sleep(1)


blinking_led()
