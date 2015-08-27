# Arduino Webapp
A webapp that helps programming arduino using a web browser

This app is supposed to run on a remote server connected to an Arduino (or similar)
board. It provides a solution to probram the Arduino board from a remote
computer using a web browser.

The use cases is an arduino connected to a Raspberry-Pi Computer.

# Requirements

## Arduino-mk

This application requires the [Arduino Makefile](https://github.com/sudar/Arduino-Makefile) to work properly, you can
either install it from repository (e.g. `apt-get install arduino-mk`) or install
it from the github repo. The second way is recommended becasue updeates:
the repository arduino-mk have issues with the Arduino Leonardo Board

## VirtualEnv
When working with python, it is reccomanded to use a [virtual environment](https://virtualenv.pypa.io/en/latest/).
Simply run 
```Bash
$ virtualenv env
$ source env/bin/activate
```
in the same forlder you downloaded the repo, then install dependences with pip


## Flask

This application uses [flask microframework](http://flask.pocoo.org/) and some flask's extension.
```Bash
(env)$ pip install flask flask-bootstrap flask-script screen flask-moment flask-sqlalchemy flask-migrate
```


# Setting up

Before running the application, you need to 
You need to export some environmental variables:
- ARDUINO_PORT -> The port where arduino is connected
- ARDUINO_MK -> The route to Arduino.mk file
- ARDUINO_BOARD -> The tag name of the board connected, (e.g., uno or leonardo)

example (with default values):
```Bash
$ export ARDUINO_PORT=/dev/ttyUSB0
$ export ARDUINO_BOARD=leonardo
$ export ARDUINO_MK=/usr/share/arduino/Arduino.mk
```

# Running the server

simply run the command

```Bash
(env)$ ./manage.py runserver -h 0.0.0.0 --threaded
```
then connect to the path http://< IP or HOSTNAME >:5000 and enjoy!

# Features

The application:
 - presents a text editor where you can write directly from the webapp Arduino code with syntax highlitghing
 - compiles and upload the code to arduino
 - Monitor Serial messages from Arduino

# Test

This Application has been test on a Respberry Pi 2 (B) running Ubunut 14.04
and an Arduino Leonardo.
Tested Clients are Google Chrome and Safari Browsers on Mac OS X Yosemite





