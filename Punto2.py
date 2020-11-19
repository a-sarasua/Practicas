import RPi.GPIO as GPIO

number = 0
pins = {
    'leds': [16, 25, 23, 24],
    'button': 12
}

GPIO.setmode(GPIO.BCM)
GPIO.setup(pins['button'], GPIO.IN)
for led in pins['leds']:
    GPIO.setup(led, GPIO.OUT)


def decimalToBcd(number):
    # Always get 4 bits
    # Get rid of first 2 chars, which are '0b'
    return bin(number)[2:].zfill(4)


while True:
    if GPIO.input(pins['button']):
        bcd = decimalToBcd(number)
        number = 0 if number == 9 else number + 1

        for i in range(4):
            led = pins['leds'][i]
            value = int(bcd[i])
            GPIO.output(led, value)
