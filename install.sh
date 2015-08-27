#setup the environment
echo 'Setting up the virtual environment ...'
easy_install pip
pip install virtuaenv
virtualenv env
source env/bin/activate

echo 'Installing Dependencies ...'
pip install flask flask-bootstrap flask-script screen flask-moment flask-sqlalchemy flask-migrate
pip install pyserial
apt-get install libdevice-serialport-perl libyaml-perl

echo 'Installing arduino-mk ...'
git clone https://github.com/sudar/Arduino-Makefile.git ../Arduino-mk

echo 'Generating Export Variables ...'
arduino_path = "${pwd}../Arduino-mk/Arduino.mk"

echo 'To end configuragion, insert this in your bashrc'
echo "export ARDUINO_MK=$arduino_path"
echo "export ARDUINO_BOARD=<YOUR BORARD> () -- e.g. export ARDUINO_BOARD=uno"
echo "export ARDUINO_PORT=<ARDUINO PORT> () -- e.g. export ARDUINO_BOARD=/dev/ttyUSB0"