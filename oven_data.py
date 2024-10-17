import requests
import serial
from time import sleep,strftime
from datetime import datetime
from random import *
'''ser = serial.Serial("COM3", baudrate=9600, timeout=1)

while True:
    bytes_serial = ser.inWaiting()
    if bytes_serial > 0:

        data = ser.readline().decode().strip()

        arr_data = data.split(",")'''

def current_time():
    return  datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def temperature():
    return round(uniform(24, 120),2)
while True:
    time = current_time()
    temp = temperature()

    # Send light level, temperature, humidity, time, and sensor ID to the server
    response = requests.post("http://127.0.0.1:5000/get_oven_data", json={
        "temperature": temperature,
        "time": time
    })
    print(f"Temperature: {temp}, Time: {time}")
    sleep(1)