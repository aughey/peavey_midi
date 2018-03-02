import mido
import sys
import time

midi_name = None
for name in mido.get_input_names():
  if name.startswith("VYPYR"):
    midi_name = name

if not midi_name:
  print("Could not find VYPYR interface")
  sys.exit(1)

input = mido.open_input(midi_name)
print("Opened: ",midi_name)

for msg in input:
   print(msg)
   print(msg.hex())
