import subprocess
import tempfile
import os
from jinja2 import Template

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
        of = open(path + "Blink.ino", "w")
        of.write(prog)
        of.close()

    def compile(self):
        os.chdir(path)
        of = open("Makefile", "w")
        make_template = Template("include {{ arduino_mk }} BOARD = {{ board }}\nPORT = {{ port }}")
        of.write(make_template.render(arduino_mk=arduino_mk, board=arduino_board, port=port))
        of.close()
        self.proc = subprocess.Popen(['make'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    def read_proc(self):
        while True:
            line = self.proc.stdout.readline()
            if line != '':
                line = line.rstrip()
                yield "data: " + line + "\n\n" 
            else:
                yield "data: " + "STOP" + "\n\n" 
                break