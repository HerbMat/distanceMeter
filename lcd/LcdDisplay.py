from RPLCD.gpio import CharLCD


class LcdDisplay:
    SPEED_OF_SOUND = 34300
    SPEED_DIVIDER = 2

    def __init__(self, cols, rows, pin_rs, pin_e, pins_data, numbering_mode):
        self.lcd = CharLCD(
            cols=cols, rows=rows, pin_rs=pin_rs, pin_e=pin_e, pins_data=pins_data, numbering_mode=numbering_mode)

    def print_in_lcd(self, text):
        self.lcd.write_string(text)
        print("Display text '{}'.".format(text))

    def clear_lcd(self):
        print("Clearing display")
        self.lcd.clear()
