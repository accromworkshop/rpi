#-------------------------------------------------------------------------------
# Name:        Python Web Application Project
# Purpose:
#
# Author:      mehmet.top
#
# Created:     23.05.2017
# Copyright:   (c) mehmet.top 2017
# Licence:     Beer License
#-------------------------------------------------------------------------------
from flask import Flask
from flask import request
from flask import render_template

import RPi.GPIO as GPIO
import dht11

APP_HOST = "localhost"
APP_PORT = 5001

GPIO_PIN_LED = 18
GPIO_PIN_SENSOR = 14

# Initialize RPi GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)



GPIO.setup(GPIO_PIN_LED, GPIO.OUT)

# Map GPIO Pin 14 to DHT11 Sensor
instance = dht11.DHT11(pin=GPIO_PIN_SENSOR)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/dashboard')
def page_dashboard():

    ledStatus = request.args.get('led')

    if ledStatus == "on":
        GPIO.output(GPIO_PIN_LED, GPIO.HIGH)
    else:
        GPIO.output(GPIO_PIN_LED, GPIO.LOW)
    
    temperature = "Error!"
    humidity    = "Error!"

    result = instance.read()
    
    while not result.is_valid():
        result = instance.read()

    temperature = result.temperature
    humidity = result.humidity

    return render_template('dashboard.html', temperature = temperature,  humidity = humidity, ledStatus = ledStatus)

if __name__ == '__main__':
    app.run(host=APP_HOST, port=APP_PORT)



