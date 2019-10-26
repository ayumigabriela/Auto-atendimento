import lcd
import time
import keyboard

def   deposit(): #to do
    lcd.lcd_write("insira ra","")
    while not keyboard.is_pressed("1"):
        continue
    lcd.lcd_write("insira ra","1")
    time.sleep(2)     # wait 2 seconds


