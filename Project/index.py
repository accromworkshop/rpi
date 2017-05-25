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
from flask import render_template

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
    return render_template('dashboard.html', temperature = 26.4,  humidity = 40.2)

if __name__ == '__main__':
    app.run()



