#-------------------------------------------------------------------------------
# Name:        Python Web Application Project
# Purpose:
#
# Author:      mehmet.top
#
# Created:     23.05.2017
# Copyright:   (c) mehmet.top 2017
# Licence:     The Beer Licence
#-------------------------------------------------------------------------------
from flask import Flask
from flask import request
from flask import render_template

import RPi.GPIO as GPIO
import dht11
import time

# Initialize RPi GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO_PIN_LED = int(18)
GPIO.setup(18, GPIO.OUT)

# Map GPIO Pin 14 to DHT11 Sensor
instance = dht11.DHT11(pin=14)

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/main')
def page_main():
    return '<html><body><div>Welcome to Main Page</div></body></html>'

@app.route('/information')
def page_information():
    return render_template('information.html')

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
    app.run()



