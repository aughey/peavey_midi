import serial

with serial.Serial("/dev/ttyAMA0", 38400) as ser:
  print("READING")
  while True:
    data = ser.read()
    print(data.hex())
