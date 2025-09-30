import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, gpio_pin, pwm_frequency, dynamic_range, verbose = False):
        self.gpio_pin = gpio_pin
        self.pwm_frequency = pwm_frequency
        self.dynamic_range = dynamic_range
        self.verbose = verbose

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_pin, GPIO.OUT, initial = 0)
        pwm = GPIO.PWM(self.gpio_pin, self.pwm_frequency)

        self.duty = 0.0
        self.pwm.start(self.duty)

    def deinit(self):
        self.duty = 0.0
        self.pwm.ChangeDutyCycle(self.duty)
        GPIO.cleanup()

    def set_voltage(self, voltage):
        if not(0 <= voltage <= self.dynamic_range):
            print(f'Напряжение выходит за динамический диапазон ЦАП (0ю00 - {dynamic_range:.2f} В)')
            print(f'Устанавливаем 0.0 В') 
            self.duty = 0
        else:
            self.duty = voltage / self.dynamic_range * 100
        self.pwm.ChangeDutyCycle(self.duty)


if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.3, True)

        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError():
                print("Вы ввели не число Попробуйте ещё раз")

    finally:
        dac.deinit() 