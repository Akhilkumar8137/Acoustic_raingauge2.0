import time
from davis_raingauge import setup_davis, get_davis_rainfall

PIN = 13   # replace with your davis_interrupt_pin

setup_davis(PIN)

print("Waiting for bucket tips...")

while True:
    time.sleep(60)   # check every 60 seconds
    rain = get_davis_rainfall()
    print(f"Rainfall in last minute = {rain} mm")
