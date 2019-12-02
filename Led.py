import os
import time


def blinking_leds():
    os.system("echo gpio | sudo tee /sys/class/leds/led1/trigger")
    time.sleep(1)
    os.system("echo input | sudo tee /sys/class/leds/led1/trigger")
    time.sleep(1)
    os.system("echo gpio | sudo tee /sys/class/leds/led1/trigger")
    time.sleep(1)
    os.system("echo cpu0 | sudo tee /sys/class/leds/led1/trigger")


blinking_leds()
