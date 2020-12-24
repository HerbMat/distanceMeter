from RPi import GPIO
from distlib.compat import raw_input
from distancemeter import DistanceMeter
from lcd import LcdDisplay
from sensor import TemperatureSensor

GPIO.setmode(GPIO.BCM)
GPIO_TRIGGER = 18
GPIO_ECHO = 24
LCD_COLUMNS = 16
LCD_ROWS = 2
LCD_PIN_RS = 26
LCD_PIN_E = 19
LCD_PINS_DATA = [13, 6, 5, 21]
LCD_NUMBERING_MODE = GPIO.BCM


def print_distance(lcd_display: LcdDisplay, distance_meter: DistanceMeter):
    print("printing distance")
    lcd_display.clear_lcd()
    measured_distance = str(distance_meter.measure_distance())
    measured_distance_text = "Compute Distance={}".format(measured_distance[:14])
    lcd_display.print_in_lcd(measured_distance_text)


def print_temperature(lcd_display: LcdDisplay, temperature_sensor: TemperatureSensor):
    print("printing temperature")
    lcd_display.clear_lcd()
    measured_temperature = str(temperature_sensor.read_temp_celsius())
    measured_temperature_text = "Temperature:    {}".format(measured_temperature[:14])
    lcd_display.print_in_lcd(measured_temperature_text)


if __name__ == '__main__':
    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
    GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    distance_meter = DistanceMeter(GPIO_TRIGGER, GPIO_ECHO)
    lcd_display = LcdDisplay(LCD_COLUMNS, LCD_ROWS, LCD_PIN_RS, LCD_PIN_E, LCD_PINS_DATA, LCD_NUMBERING_MODE)
    temperature_sensor = TemperatureSensor()

    GPIO.add_event_detect(
        16, GPIO.RISING, callback=lambda x: print_distance(lcd_display, distance_meter), bouncetime=200)
    GPIO.add_event_detect(
        20, GPIO.RISING, callback=lambda x: print_temperature(lcd_display, temperature_sensor), bouncetime=200)

    raw_input('Click to close: ')
    lcd_display.clear_lcd()
    GPIO.cleanup()
