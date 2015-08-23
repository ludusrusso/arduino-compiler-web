# Arduino Webapp
A webapp that help programming arduino using a web browser

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

This application uses [flask microframework](http://flask.pocoo.org/) to accomplish web tasks, you
can simply download it with the commabnd pip install flask. The application
also need flask-bootstrap and flask-script.
```Bash
(env)$ pip intall flask flask-bootstrap flask-script
```


# Setting up

Before running the application, you need to 
You need to export some environmental variables:
ARDUINO_PORT -> The port where arduino is connected
ARDUINO_MK -> The route to Arduino.mk file
ARDUINO_BOARD -> The tag name of the board connected, (e.g., uno or leonardo)

example (with default values):
```Bash
$ source ARDUINO_PORT=/dev/ttyUSB0
$ source ARDUINO_BOARD=leonardo
$ source ARDUINO_MK=/usr/share/arduino/Arduino.mk
```

# Running the server

simply run the command

```Bash
(env)$ ./manager runserver -h 0.0.0.0
```
then connect to the path http://< IP or HOSTNAME >:5000 and enjoy!










