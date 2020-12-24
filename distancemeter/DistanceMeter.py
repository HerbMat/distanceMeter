import RPi.GPIO as GPIO
import time


class DistanceMeter:
    SPEED_OF_SOUND = 34300
    SPEED_DIVIDER = 2

    def __init__(self, gpio_trigger, gpio_echo):
        self.gpio_trigger = gpio_trigger
        self.gpio_echo = gpio_echo
        GPIO.setup(gpio_trigger, GPIO.OUT)
        GPIO.setup(gpio_echo, GPIO.IN)

    def measure_distance(self):
        GPIO.output(self.gpio_trigger, True)
        time.sleep(0.00001)
        GPIO.output(self.gpio_trigger, False)

        start_time = time.time()
        stop_time = time.time()

        while GPIO.input(self.gpio_echo) == 0:
            stop_time = time.time()
        while GPIO.input(self.gpio_echo) == 1:
            stop_time = time.time()

        time_elapsed = stop_time - start_time
        distance = (time_elapsed * self.SPEED_OF_SOUND) / self.SPEED_DIVIDER

        return distance
