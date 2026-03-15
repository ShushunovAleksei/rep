import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
       
        self.gpio_bits = gpio_pin
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        self.freq = pwm_frequency
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0) 
        
    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()
        
    def set_voltage(self, voltage):
        if (0.0 <= voltage <= dynamic_range):
            duty_cycle = (voltage / self.dynamic_range * 100)
        else:
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {dynamic_range:.2f} В)")
            print("Устанавлниваем 0.0 В")
            duty_cycle = 0
        self.pwm.ChangeDutyCycle(duty_cycle)
        if self.verbose:
            print(f"Коэффициент заполнения {duty_cycle:.2f}%")
            
    
        

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

