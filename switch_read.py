import serial
import sys

with serial.Serial("/dev/ttyAMA0", 38400) as ser:
  while True:
    data = ser.read()
    if data[0] == 0xc0:
      data = ser.read()
      print(data.hex())
      sys.stdout.flush()
