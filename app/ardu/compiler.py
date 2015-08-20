import subprocess
import tempfile
import os
from flask import render_template

path = '/tmp/web_arduino/'
if not os.path.isdir(path):
    os.mkdir(path)

arduino_board = os.environ.get('ARDUINO_BOARD') or 'leonardo'
port = os.environ.get('ARDUINO_PORT') or '/dev/ttyUSB0'
arduino_mk = os.environ.get('ARDUINO_MK') or '/usr/share/arduino/Arduino.mk'

class Compiler:
    def __init__(self):
        pass

    def save(self, prog):
        of = open(path + "program.ino", "w")
        of.write(prog)
        of.close()

    def compile(self):
        os.chdir(path)
        of = open("Makefile", "w")
        of.write(render_template('ardu/Makefile', mk=arduino_mk, board=arduino_board, port=port, libs=''))
        of.close()
        self.proc = subprocess.Popen(['make', 'upload'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def read_proc(self):
        while True:
            line = self.proc.stdout.readline()
            if line != '':
                line = line.rstrip()
                yield "data: " + line + "\n\n" 
            else:
                yield "data: " + "STOP" + "\n\n" 
                break