import RPi.GPIO as GPIO
import time

count = 0

def bucket_tipped(channel):
    global count

    time.sleep(0.02)  # 20 ms debounce check

    if GPIO.input(channel) == GPIO.LOW:
        print("COUNT BEFORE RESET =", count)
        count += 1

def setup_davis(interrupt_pin):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(interrupt_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    GPIO.add_event_detect(
        interrupt_pin,
        GPIO.RISING,
        callback=bucket_tipped,
        bouncetime=500
    )


def get_davis_rainfall():
    global count

    rainfall = count * 0.2

    count = 0

    return rainfall
