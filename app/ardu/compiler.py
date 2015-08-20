import subprocess
import tempfile
import os

path = '/tmp/web_arduino/'
if not os.path.isdir(path):
    os.mkdir(path)


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
        make = "include /Users/ludus/develop/arduino_ws/Arduino-Makefile/Arduino.mk \n BOARD = uno \n PORT = /dev/tty.usbmodem*"
        of.write(make)
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