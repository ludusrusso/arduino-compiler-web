import subprocess
import tempfile
import os
from flask import render_template

import serial

path = '/tmp/web_arduino/'
if not os.path.isdir(path):
    os.mkdir(path)

arduino_board = os.environ.get('ARDUINO_BOARD') or 'leonardo'
port = os.environ.get('ARDUINO_PORT') or '/dev/ttyUSB0'
arduino_mk = os.environ.get('ARDUINO_MK') or '/usr/share/arduino/Arduino.mk'

class Compiler:
    def __init__(self):
        self.read = False
        pass

    def save(self, prog):
        of = open(path + "program.ino", "w")
        of.write(prog)
        of.close()

    def compile(self):
        if (self.read == True):
            return
        os.chdir(path)
        of = open("Makefile", "w")
        of.write(render_template('ardu/Makefile', mk=arduino_mk, board=arduino_board, port=port, libs=''))
        of.close()
        self.proc = subprocess.Popen(['make', 'upload'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def monitor_open(self):
        if (self.read == True):
            return
        ser = serial.Serial(port, 9600, timeout=1)
        self.read = True
        while self.read:
            yield "data: " + ser.readline().rstrip() + "\n\n"
        ser.close()
        yield "data: " + "STOP" + "\n\n" 

    def monitor_close(self):
        self.read = False

    def read_proc(self):
        while True:
            line = self.proc.stdout.readline()
            if line != '':
                line = line.rstrip()
                yield "data: " + line + "\n\n" 
            else:
                yield "data: " + "STOP" + "\n\n" 
                break
        self.read = False