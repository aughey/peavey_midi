import mido
import sys
import time

midi_name = None
for name in mido.get_output_names():
  if name.startswith("VYPYR"):
    midi_name = name

if not midi_name:
  print("Could not find VYPYR interface")
  sys.exit(1)

output = mido.open_output(midi_name)

def send_value(value):
    msg = mido.Message("control_change", control=20, value=value)
    output.send(msg)
    time.sleep(0.01)

while True:
  for value in range(1,127):
    send_value(value)
  
  for value in range(127,0,-1):
    send_value(value)
