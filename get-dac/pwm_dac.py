import RPi.GPIO as GPIO
import time
class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
       
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0) 
        
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
        
    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
            print("Устанавлниваем 0.0 В")
            return 0
    number = int(voltage / dynamic_range * 255)
    self.set_number(number)
        

if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.290, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()

